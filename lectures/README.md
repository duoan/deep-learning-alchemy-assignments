# CS312 Course Materials Index

Organized by assignment scope from the [course website](https://deep-learning-alchemy.github.io/). Papers are assigned to lectures according to the reading lists in the course schedule. Last verified: 2026-11-12.

All 64 original files have been retained, including 25 arXiv papers that have been renamed. The contents of the PDFs, PPTX files, and saved web resources are unchanged.

## Directory Structure and Naming

- Each assignment PDF is stored at the root of its assignment directory. Lecture slides are stored in the corresponding `lecture_XX_*/` directory.
- Papers are stored in each lecture's `papers/` directory. Quizzes and answer slides are stored in the assignment's `quizzes/` directory.
- LLMs 101 materials are stored in A1's `supplementary/` directory. The saved Muon web page and its complete resource directory are stored in Lecture 04's `readings/` directory.
- Paper filenames follow `Lecture NN <lecture name> - <full paper title> - <original arXiv basename>.pdf`. The arXiv version number is retained. Colons and question marks in titles are replaced with ` - `.
- Original paths, new paths, and SHA-256 hashes are recorded in [file_manifest.json](file_manifest.json).

| Assignment | Scope | Lectures | Directory |
| --- | --- | --- | --- |
| A1 | Basics: Hyperparameter tuning and scaling | 01, 02 | [a1_basics](a1_basics/) |
| A2 | Optimization 1: Hyperparameter invariants | 03, 04 | [a2_hyperparameter_scaling](a2_hyperparameter_scaling/) |
| A3 | Optimization 2: Loss landscapes | 05, 06 | [a3_optimization2](a3_optimization2/) |
| A4 | Architecture 1: Stability across depth/time | 07, 08 | [a4_stability](a4_stability/) |
| A5 | Architecture 2: Extending model capacity | 09 | [a5_capacity](a5_capacity/) |
| A6 | Generalization: Data-efficient algorithms | 10 | [a6_generalization](a6_generalization/) |

## Course Materials Not Available Locally

- Lecture 02 slides were missing from the original local directory. See the [official PDF](https://deep-learning-alchemy.github.io/assets/slides/lecture_02.pdf). All three assigned papers are available locally.
- Lecture 03's [Weight decay blog](https://whenwen.github.io/wd_blog/public/weight-decay-part-2.html) and Lecture 08's [DeltaNet Explained](https://sustcsonglin.github.io/blog/2024/deltanet-1/) were not present in the original directory.
- As of the verification date, the website lists the November 17 Generalization lecture materials and A7 Exotic materials as TBA. No corresponding files are available locally.

## Lectures and Papers

### Lecture 01: Introduction

2026-09-22 · [Local directory](a1_basics/lecture_01_introduction/)

- Slides: [PDF](a1_basics/lecture_01_introduction/lecture_01.pdf)

### Lecture 02: Basics

2026-09-24 · [Local directory](a1_basics/lecture_02_basics/)

- [Predictable Scale: Part I, Step Law -- Optimal Hyperparameter Scaling Law in Large Language Model Pretraining](a1_basics/lecture_02_basics/papers/Lecture%2002%20Basics%20-%20Predictable%20Scale%20-%20Part%20I%2C%20Step%20Law%20--%20Optimal%20Hyperparameter%20Scaling%20Law%20in%20Large%20Language%20Model%20Pretraining%20-%202503.04715v7.pdf) · [arXiv 2503.04715v7](https://arxiv.org/abs/2503.04715v7)
- [Scaling Laws for Neural Language Models](a1_basics/lecture_02_basics/papers/Lecture%2002%20Basics%20-%20Scaling%20Laws%20for%20Neural%20Language%20Models%20-%202001.08361v1.pdf) · [arXiv 2001.08361v1](https://arxiv.org/abs/2001.08361v1)
- [Nondeterminism and Instability in Neural Network Optimization](a1_basics/lecture_02_basics/papers/Lecture%2002%20Basics%20-%20Nondeterminism%20and%20Instability%20in%20Neural%20Network%20Optimization%20-%202103.04514v3.pdf) · [arXiv 2103.04514v3](https://arxiv.org/abs/2103.04514v3)

### Lecture 03: Optimizers 1: Invariances (and Hyperparameters)

2026-10-01 · [Local directory](a2_hyperparameter_scaling/lecture_03_optimizer_invariances/)

- Slides: [PDF](a2_hyperparameter_scaling/lecture_03_optimizer_invariances/lecture_03.pdf)
- Slides: [PPTX](a2_hyperparameter_scaling/lecture_03_optimizer_invariances/lecture_03.pptx)
- [Which Algorithmic Choices Matter at Which Batch Sizes? Insights From a Noisy Quadratic Model](a2_hyperparameter_scaling/lecture_03_optimizer_invariances/papers/Lecture%2003%20Optimizers%201%20-%20Invariances%20%28and%20Hyperparameters%29%20-%20Which%20Algorithmic%20Choices%20Matter%20at%20Which%20Batch%20Sizes%20-%20Insights%20From%20a%20Noisy%20Quadratic%20Model%20-%201907.04164v2.pdf) · [arXiv 1907.04164v2](https://arxiv.org/abs/1907.04164v2)
- [Fantastic Pretraining Optimizers and Where to Find Them II: Hyperball Optimization](a2_hyperparameter_scaling/lecture_03_optimizer_invariances/papers/Lecture%2003%20Optimizers%201%20-%20Invariances%20%28and%20Hyperparameters%29%20-%20Fantastic%20Pretraining%20Optimizers%20and%20Where%20to%20Find%20Them%20II%20-%20Hyperball%20Optimization%20-%202606.16899v2.pdf) · [arXiv 2606.16899v2](https://arxiv.org/abs/2606.16899v2)
- Supplementary reading: [Weight decay blog (online)](https://whenwen.github.io/wd_blog/public/weight-decay-part-2.html)

### Lecture 04: Optimizers 1: Parametrization and Preconditioning

2026-10-06 · [Local directory](a2_hyperparameter_scaling/lecture_04_parametrization_and_preconditioning/)

- Slides: [PDF](a2_hyperparameter_scaling/lecture_04_parametrization_and_preconditioning/lecture_04.pdf)
- [Scaling Exponents Across Parameterizations and Optimizers](a2_hyperparameter_scaling/lecture_04_parametrization_and_preconditioning/papers/Lecture%2004%20Optimizers%201%20-%20Parametrization%20and%20Preconditioning%20-%20Scaling%20Exponents%20Across%20Parameterizations%20and%20Optimizers%20-%202407.05872v2.pdf) · [arXiv 2407.05872v2](https://arxiv.org/abs/2407.05872v2)
- [Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer](a2_hyperparameter_scaling/lecture_04_parametrization_and_preconditioning/papers/Lecture%2004%20Optimizers%201%20-%20Parametrization%20and%20Preconditioning%20-%20Tensor%20Programs%20V%20-%20Tuning%20Large%20Neural%20Networks%20via%20Zero-Shot%20Hyperparameter%20Transfer%20-%202203.03466v2.pdf) · [arXiv 2203.03466v2](https://arxiv.org/abs/2203.03466v2)
- Supplementary reading: [Muon: An optimizer for hidden layers in neural networks (offline web page)](a2_hyperparameter_scaling/lecture_04_parametrization_and_preconditioning/readings/Muon_%20An%20optimizer%20for%20hidden%20layers%20in%20neural%20networks%20_%20Keller%20Jordan%20blog.html)

### Lecture 05: Loss Landscapes Part 1 - Basins, River Valley, Critical Points

2026-10-13 · [Local directory](a3_optimization2/lecture_05_loss_landscape_geometry/)

- Slides: [PDF](a3_optimization2/lecture_05_loss_landscape_geometry/lecture_05.pdf)
- [Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs](a3_optimization2/lecture_05_loss_landscape_geometry/papers/Lecture%2005%20Loss%20Landscapes%20Part%201%20-%20Basins%2C%20River%20Valley%2C%20Critical%20Points%20-%20Loss%20Surfaces%2C%20Mode%20Connectivity%2C%20and%20Fast%20Ensembling%20of%20DNNs%20-%201802.10026v4.pdf) · [arXiv 1802.10026v4](https://arxiv.org/abs/1802.10026v4)
- [Understanding Warmup-Stable-Decay Learning Rates: A River Valley Loss Landscape Perspective](a3_optimization2/lecture_05_loss_landscape_geometry/papers/Lecture%2005%20Loss%20Landscapes%20Part%201%20-%20Basins%2C%20River%20Valley%2C%20Critical%20Points%20-%20Understanding%20Warmup-Stable-Decay%20Learning%20Rates%20-%20A%20River%20Valley%20Loss%20Landscape%20Perspective%20-%202410.05192v3.pdf) · [arXiv 2410.05192v3](https://arxiv.org/abs/2410.05192v3)
- [Identifying and attacking the saddle point problem in high-dimensional non-convex optimization](a3_optimization2/lecture_05_loss_landscape_geometry/papers/Lecture%2005%20Loss%20Landscapes%20Part%201%20-%20Basins%2C%20River%20Valley%2C%20Critical%20Points%20-%20Identifying%20and%20attacking%20the%20saddle%20point%20problem%20in%20high-dimensional%20non-convex%20optimization%20-%201406.2572v1.pdf) · [arXiv 1406.2572v1](https://arxiv.org/abs/1406.2572v1)

### Lecture 06: Loss Landscapes Part 2 - Edge of Stability

2026-10-15 · [Local directory](a3_optimization2/lecture_06_sharpness_and_stability/)

- Slides: [PDF](a3_optimization2/lecture_06_sharpness_and_stability/lecture_06.pdf)
- Slides: [PPTX](a3_optimization2/lecture_06_sharpness_and_stability/lecture_06.pptx)
- [Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability](a3_optimization2/lecture_06_sharpness_and_stability/papers/Lecture%2006%20Loss%20Landscapes%20Part%202%20-%20Edge%20of%20Stability%20-%20Gradient%20Descent%20on%20Neural%20Networks%20Typically%20Occurs%20at%20the%20Edge%20of%20Stability%20-%202103.00065v3.pdf) · [arXiv 2103.00065v3](https://arxiv.org/abs/2103.00065v3)
- [Understanding Optimization in Deep Learning with Central Flows](a3_optimization2/lecture_06_sharpness_and_stability/papers/Lecture%2006%20Loss%20Landscapes%20Part%202%20-%20Edge%20of%20Stability%20-%20Understanding%20Optimization%20in%20Deep%20Learning%20with%20Central%20Flows%20-%202410.24206v2.pdf) · [arXiv 2410.24206v2](https://arxiv.org/abs/2410.24206v2)
- [Sharpness-Aware Minimization for Efficiently Improving Generalization](a3_optimization2/lecture_06_sharpness_and_stability/papers/Lecture%2006%20Loss%20Landscapes%20Part%202%20-%20Edge%20of%20Stability%20-%20Sharpness-Aware%20Minimization%20for%20Efficiently%20Improving%20Generalization%20-%202010.01412v3.pdf) · [arXiv 2010.01412v3](https://arxiv.org/abs/2010.01412v3)

### Lecture 07: Architecture 1: Signal Propagation in Depth

2026-10-22 · [Local directory](a4_stability/lecture_07_signal_propagation_in_depth/)

- Slides: [PDF](a4_stability/lecture_07_signal_propagation_in_depth/lecture_07.pdf)
- [Identity Mappings in Deep Residual Networks](a4_stability/lecture_07_signal_propagation_in_depth/papers/Lecture%2007%20Architecture%201%20-%20Signal%20Propagation%20in%20Depth%20-%20Identity%20Mappings%20in%20Deep%20Residual%20Networks%20-%201603.05027v3.pdf) · [arXiv 1603.05027v3](https://arxiv.org/abs/1603.05027v3)
- [Deep Information Propagation](a4_stability/lecture_07_signal_propagation_in_depth/papers/Lecture%2007%20Architecture%201%20-%20Signal%20Propagation%20in%20Depth%20-%20Deep%20Information%20Propagation%20-%201611.01232v2.pdf) · [arXiv 1611.01232v2](https://arxiv.org/abs/1611.01232v2)
- [mHC: Manifold-Constrained Hyper-Connections](a4_stability/lecture_07_signal_propagation_in_depth/papers/Lecture%2007%20Architecture%201%20-%20Signal%20Propagation%20in%20Depth%20-%20mHC%20-%20Manifold-Constrained%20Hyper-Connections%20-%202512.24880v2.pdf) · [arXiv 2512.24880v2](https://arxiv.org/abs/2512.24880v2)

### Lecture 08: Architecture 1: Signal Propagation in Time

2026-10-27 · [Local directory](a4_stability/lecture_08_signal_propagation_in_time/)

- Slides: [PDF](a4_stability/lecture_08_signal_propagation_in_time/lecture_08.pdf)
- [On the difficulty of training Recurrent Neural Networks](a4_stability/lecture_08_signal_propagation_in_time/papers/Lecture%2008%20Architecture%201%20-%20Signal%20Propagation%20in%20Time%20-%20On%20the%20difficulty%20of%20training%20Recurrent%20Neural%20Networks%20-%201211.5063v2.pdf) · [arXiv 1211.5063v2](https://arxiv.org/abs/1211.5063v2)
- [When Attention Sink Emerges in Language Models: An Empirical View](a4_stability/lecture_08_signal_propagation_in_time/papers/Lecture%2008%20Architecture%201%20-%20Signal%20Propagation%20in%20Time%20-%20When%20Attention%20Sink%20Emerges%20in%20Language%20Models%20-%20An%20Empirical%20View%20-%202410.10781v2.pdf) · [arXiv 2410.10781v2](https://arxiv.org/abs/2410.10781v2)
- Supplementary reading: [DeltaNet Explained (online)](https://sustcsonglin.github.io/blog/2024/deltanet-1/)

### Lecture 09: Architecture 2: Expressivity

2026-11-05 · [Local directory](a5_capacity/lecture_09_expressivity/)

- Slides: [PDF](a5_capacity/lecture_09_expressivity/lecture_09.pdf)
- [Benefits of depth in neural networks](a5_capacity/lecture_09_expressivity/papers/Lecture%2009%20Architecture%202%20-%20Expressivity%20-%20Benefits%20of%20depth%20in%20neural%20networks%20-%201602.04485v2.pdf) · [arXiv 1602.04485v2](https://arxiv.org/abs/1602.04485v2)
- [Complexity of Linear Regions in Deep Networks](a5_capacity/lecture_09_expressivity/papers/Lecture%2009%20Architecture%202%20-%20Expressivity%20-%20Complexity%20of%20Linear%20Regions%20in%20Deep%20Networks%20-%201901.09021v2.pdf) · [arXiv 1901.09021v2](https://arxiv.org/abs/1901.09021v2)
- [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](a5_capacity/lecture_09_expressivity/papers/Lecture%2009%20Architecture%202%20-%20Expressivity%20-%20Breaking%20the%20Softmax%20Bottleneck%20-%20A%20High-Rank%20RNN%20Language%20Model%20-%201711.03953v4.pdf) · [arXiv 1711.03953v4](https://arxiv.org/abs/1711.03953v4)
- [Transformers Learn Shortcuts to Automata](a5_capacity/lecture_09_expressivity/papers/Lecture%2009%20Architecture%202%20-%20Expressivity%20-%20Transformers%20Learn%20Shortcuts%20to%20Automata%20-%202210.10749v2.pdf) · [arXiv 2210.10749v2](https://arxiv.org/abs/2210.10749v2)

### Lecture 10: Generalization Lecture 1 - Regularization and fine-tuning

2026-11-12 · [Local directory](a6_generalization/lecture_10_regularization_and_fine_tuning/)

- Slides: [PDF](a6_generalization/lecture_10_regularization_and_fine_tuning/lecture_10.pdf)
- [Surprises in High-Dimensional Ridgeless Least Squares Interpolation](a6_generalization/lecture_10_regularization_and_fine_tuning/papers/Lecture%2010%20Generalization%20Lecture%201%20-%20Regularization%20and%20fine-tuning%20-%20Surprises%20in%20High-Dimensional%20Ridgeless%20Least%20Squares%20Interpolation%20-%201903.08560v5.pdf) · [arXiv 1903.08560v5](https://arxiv.org/abs/1903.08560v5)
- [Pre-training under infinite compute](a6_generalization/lecture_10_regularization_and_fine_tuning/papers/Lecture%2010%20Generalization%20Lecture%201%20-%20Regularization%20and%20fine-tuning%20-%20Pre-training%20under%20infinite%20compute%20-%202509.14786v1.pdf) · [arXiv 2509.14786v1](https://arxiv.org/abs/2509.14786v1)
- [Scaling Laws for Transfer](a6_generalization/lecture_10_regularization_and_fine_tuning/papers/Lecture%2010%20Generalization%20Lecture%201%20-%20Regularization%20and%20fine-tuning%20-%20Scaling%20Laws%20for%20Transfer%20-%202102.01293v1.pdf) · [arXiv 2102.01293v1](https://arxiv.org/abs/2102.01293v1)
