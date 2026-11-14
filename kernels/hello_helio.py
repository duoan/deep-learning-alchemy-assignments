import os

os.environ["HELION_BACKEND"] = "metal"
import helion
import helion.language as hl
import torch


@helion.kernel(
    # Settings: Control compilation behavior
    autotune_effort="none",  # Skip autotuning for development
    print_output_code=True,  # Debug: show generated code
    # Config: Control GPU execution (when not using default)
    # config=helion.Config(block_sizes=[64, 32], num_warps=8)
)
def matmul(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    m, k = x.size()
    k, n = y.size()
    out = torch.empty([m, n], dtype=x.dtype, device=x.device)

    for tile_m, tile_n in hl.tile([m, n]):
        acc = hl.zeros([tile_m, tile_n], dtype=torch.float32)
        for tile_k in hl.tile(k):
            acc = torch.addmm(acc, x[tile_m, tile_k], y[tile_k, tile_n])
        out[tile_m, tile_n] = acc

    return out


if __name__ == '__main__':
    A = torch.randn([2048, 2048], device="mps")
    B = torch.randn([2048, 2048], device="mps")
    out = matmul(A, B)
    torch.testing.assert_close(out, torch.matmul(A, B), rtol=1e-5, atol=1e-5)
