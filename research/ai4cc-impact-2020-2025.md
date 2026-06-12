# AI4CC Accepted Papers (2020-2025): Impact & Lineage

## 0. Prologue — the 2019 tutorial that started it

Before AI4CC became a paper workshop it began as the **"Deep Learning for Content Creation" tutorial at CVPR 2019** (with NVIDIA). Its lecture lineup reads as a who's-who of generative content creation — many went on to define the field, and several became AI4CC organizers or speakers:

| Lecturer (2019) | Talk | Known for / since |
|---|---|---|
| Phillip Isola (MIT) | Paired & Unpaired Image Translation | pix2pix / CycleGAN |
| Ming-Yu Liu (NVIDIA) | FUNIT | GauGAN/SPADE, NVIDIA Deep Imagination, eDiff-I |
| Tero Karras (NVIDIA) | — | StyleGAN / ProGAN / StyleGAN2–3 |
| Sanja Fidler (NVIDIA/Toronto) | Meta-Sim | NVIDIA Toronto AI, GET3D |
| Taesung Park (Berkeley) | — | CycleGAN/GauGAN → co-founder of **Reve** (AI4CC 2026 speaker) |
| Ting-Chun Wang (NVIDIA) | vid2vid | pix2pixHD, video synthesis |
| Jun-Yan Zhu (MIT) | Visualizing & Understanding GANs | CycleGAN → CMU, **AI4CC organizer** |
| Sylvain Paris / Eli Shechtman (Adobe) | Stylization | Adobe generative imaging |
| Deqing Sun (Google) | Opening | **AI4CC organizer every year** |
| James Tompkin (Brown) | Improving Image Translation | **AI4CC organizer** |

The tutorial had no paper track, so the analysis below covers the **185 accepted papers from 2020–2025**.

---


## 1. Executive Summary

This report traces the impact and intellectual lineage of every accepted paper at the AI for Content Creation (AI4CC) workshop from 2020 through 2025, drawn from per-paper impact records (citation counts, "highly influential" citation counts, awards, and downstream/author-follow-up lineages).

**Track record at a glance**

- **Total papers covered:** 185 across six years (2020-2025), plus one 2019-dated record (*Semantic Hierarchy Emerges in Deep Generative Representations*) carried in the set.
- **Tier distribution** (tier 3 = landmark / landmark-lineage; tier 2 = solid/notable; tier 1 = ordinary):
  - **Tier 3 (landmark or landmark-lineage):** 54 papers
  - **Tier 2 (solid, notable):** 89 papers
  - **Tier 1 (ordinary impact):** 42 papers
- **Awarded papers:** at least 20 carry an award flag (AI4CC Best Paper, Runner-up, Best Poster, Best Presentation, Audience Choice, oral) or a downstream main-conference honor (CVPR Highlight/Oral, CRV Best Paper).
- **Citation heavyweights (verified counts):** StarGAN v2 (~2,080), InterFaceGAN (~1,080), Dream Fields (~657), Image2StyleGAN++ (~591), Dataset Distillation by Matching Training Trajectories (~573), StyleSDF (~398), DL3DV-10K (~411), A-NeRF (~308), SEAN (~280), SpaText (~270), DIGAN (~229), Semantic Hierarchy (~212), Regularizing GANs under Limited Data / LeCam (~177), StyleMapGAN (~168), T2V-CompBench (~132), MagicAnimate (~127), GIRAFFE HD (~114), Visual Prompt Tuning for Generative Transfer (~116), LF-Font (~111), COCO-FUNIT (~93).

**Patterns**

1. **Workshop-as-precursor.** A recurring structure is that the AI4CC entry is the *early/abstract/short version* of a paper that later landed at a top venue (CVPR, ECCV, AAAI, ICLR, WACV, BMVC) and carries the real citation weight — e.g., OC-GAN → AAAI 2021, DM-Font → ECCV 2020, FixNoise → CVPR 2023, "Tax-free" 3DMM → WACV 2024, Dream Fields → DreamFusion, IMMA → ECCV 2024, FlowMDM → CVPR 2024.
2. **Lineage often beats raw citations.** Several near-zero-citation papers sit at the head of landmark trajectories: *Network Fusion with Conditional INNs* (Esser/Rombach/Ommer → VQGAN → Stable Diffusion → Black Forest Labs), *Improved Image Generation via Sparse Modeling* (Ganz/Elad → CLIPAG), *MorphGAN* (Ruiz → DreamBooth), *ClickDiffusion* (Helbling/Chau → ConceptAttention).

**Standout lineages**

- **CompVis / Stable Diffusion thread:** *Network Fusion with Conditional INNs* (2020), *High-Resolution Complex Scene Synthesis with Transformers* (2021, Best Paper), and *Towards Unified Keyframe Propagation Models* (2022) all trace to Esser/Rombach/Ommer — the team behind VQGAN, Latent Diffusion / Stable Diffusion, Runway Gen-1/2, SD3, and Black Forest Labs (FLUX).
- **GenForce GAN-interpretability thread:** *Semantic Hierarchy* (2019), *Interpreting the Latent Space of GANs / InterFaceGAN* (2020), *Decorating Your Own Bedroom* (2021), *Generative Hierarchical Features* (2021), and *Spatial Steerability of GANs* (2024) — Shen/Yang/Zhou and collaborators, foundational to controllable generation and (via Jianyuan Wang) VGGT (CVPR 2025 Best Paper).
- **Text-to-3D / SDS thread:** *Dream Fields* (2022, Best Poster) → DreamFusion (SDS), feeding *CLIP-Actor*, *Paint-it*, *Posterior Distillation Sampling*, *As-Plausible-As-Possible*, *Deep Geometric Moments*.
- **Google masked-generative / video thread:** *BLT*, *Visual Prompt Tuning for Generative Transfer*, *Discrete Predictor-Corrector Diffusion*, *CamViG*, *Text Prompting for Multi-Concept Video*, *MALT Diffusion* — the MaskGIT/Muse/VideoPoet/W.A.L.T cluster (Chang, Jiang, Essa, Lezama, Sohn, Yu).
- **NAVER/Clova generative thread:** StarGAN v2, StyleMapGAN, DM-Font/LF-Font, Visual Style Prompting, Cross-Domain Style Mixing/WebtoonMe, Custom-Edit, Enhancing Creative Generation.
- **Laval lighting-estimation thread:** *Overparameterization Improves StyleGAN Inversion*, *EverLight*, *Towards a Perceptual Evaluation Framework for Lighting Estimation* (Lalonde lab).

---

## 2. Most Influential Papers (Top ~20)

Ranked by tier, then by verified citation count. "Cites / Influential" are Semantic Scholar counts where available; "n/a" means the record's count was null (not fabricated).

### 1. **StarGAN v2: Diverse Image Synthesis for Multiple Domains**
*Year:* 2020 · *Award:* none · *Tier 3* · *Cites / Influential:* 2,080 / 410
A canonical CVPR 2020 baseline for diverse multi-domain image translation and the source of the widely reused AFHQ animal-faces dataset. Its open-source release by Clova AI/NAVER made it a heavily-built-upon foundation across the GAN-to-diffusion editing era. It is the direct successor to the team's own StarGAN (CVPR 2018); senior author Yunjey Choi remained a leading NAVER AI Lab generative-models researcher (later *Visual Style Prompting*, itself an AI4CC 2024 Best Paper). Cited across the StyleGAN2 family and countless image-to-image and diffusion image-editing works.

### 2. **Interpreting the Latent Space of GANs for Semantic Face Editing (InterFaceGAN)**
*Year:* 2020 · *Award:* none · *Tier 3* · *Cites / Influential:* 1,080 / 186
Foundational GenForce (Shen, Gu, Tang, Zhou; CUHK) work showing GAN latent spaces encode disentangled, linearly-separable semantic attributes, enabling controllable face editing on any pretrained StyleGAN/PGGAN. It seeded an entire latent-space-editing subfield: the same authors' SeFa (CVPR 2021), the TPAMI InterFaceGAN extension, and In-Domain GAN Inversion (ECCV 2020), alongside GANSpace, StyleFlow, and StyleCLIP. First author Yujun Shen became a leading generative-model researcher (Ant Group); Bolei Zhou is now UCLA faculty. Landmark lineage.

### 3. **Zero-Shot Text-Guided Object Generation with Dream Fields**
*Year:* 2022 · *Award:* Best poster · *Tier 3* · *Cites / Influential:* 657 / 36
The foundational CLIP-guided text-to-3D method (Jain, Mildenhall, Barron, Abbeel, Poole): optimize a NeRF so its renders score highly under CLIP. The same core authors then produced **DreamFusion**, which introduced Score Distillation Sampling (SDS) and ignited the entire text-to-3D explosion (Magic3D, Score Jacobian Chaining, Latent-NeRF, DreamGaussian, Fantasia3D). One of the most consequential single-paper-to-subfield lineages in the set.

### 4. **Image2StyleGAN++: How to Edit the Embedded Images?**
*Year:* 2020 · *Award:* none · *Tier 3* · *Cites / Influential:* 591 / 49
CVPR 2020 work (KAUST/Wonka) extending the W+ embedding with noise optimization and local edits, helping define the GAN-inversion-for-editing paradigm. Direct successor to Image2StyleGAN (ICCV 2019) and precursor to the authors' highly cited StyleFlow (TOG 2021) and StyleGAN-NADA / 3D-aware GAN work. Cited across the pSp/e4e/encoder-based GAN-inversion literature.

### 5. **Dataset Distillation by Matching Training Trajectories (MTT)**
*Year:* 2022 · *Award:* none · *Tier 3* · *Cites / Influential:* 573 / 163
The dominant baseline for the entire dataset-distillation subfield, from a CMU-MIT-Berkeley team (Cazenavette, Wang, Torralba, Efros, Zhu). Spawned a large follow-up body (FTD, TESLA, DATM, Automatic Training Trajectories) and the authors' own *Generalizing Dataset Distillation via Deep Generative Prior* (CVPR 2023). A reference point for distillation benchmarks.

### 6. **DL3DV-10K: A Large-Scale Scene Dataset for Deep Learning-based 3D Vision**
*Year:* 2024 · *Award:* none · *Tier 3* · *Cites / Influential:* 411 / n/a
A landmark real-scene dataset (10,510 videos, 51.2M frames) from the Benes and Bera groups. It became a standard benchmark and pretraining corpus for NeRF, generalizable NeRF, and 3D Gaussian Splatting; the DL3DV-Benchmark is widely used to evaluate ZipNeRF, Mip-NeRF 360, Instant-NGP, and 3DGS. Cited by numerous NVS/3DGS works (e.g., 3DGS-Enhancer, "NeRF Is a Valuable Assistant for 3DGS").

### 7. **StyleSDF: High-Resolution 3D-Consistent Image and Geometry Generation**
*Year:* 2022 · *Award:* none · *Tier 3* · *Cites / Influential:* 398 / 54
A 3D-aware GAN fusing an SDF-based 3D representation with a StyleGAN2 generator for view-consistent face/geometry generation — a canonical reference alongside EG3D/StyleNeRF/pi-GAN. Co-authored by DeepSDF creator Jeong Joon Park (now Michigan; DiffusionPDE, NeurIPS 2024) and Adobe's Eli Shechtman; UW's Kemelmacher-Shlizerman lab. Seeded the SDF-based 3D generative thread (e.g., SDF-StyleGAN).

### 8. **A-NeRF: Articulated Neural Radiance Fields for Learning Human Shape, Appearance, and Pose**
*Year:* 2022 · *Award:* none · *Tier 3* · *Cites / Influential:* 308 / 23
A foundational articulated-human-NeRF paper (NeurIPS 2021) introducing skeleton-relative reparameterization to learn a body model from monocular video. A core precursor in the animatable/articulated NeRF-avatar line; lead author Shih-Yang Su followed with DANBO (ECCV 2022). Widely cited across HumanNeRF, Neural Body, and Animatable NeRF.

### 9. **SEAN: Image Synthesis with Semantic Region-Adaptive Normalization**
*Year:* 2020 · *Award:* none · *Tier 3* (record tier 2) · *Cites / Influential:* 280 / 50
A CVPR 2020 Oral (KAUST/Wonka) introducing semantic region-adaptive normalization, extending SPADE/GauGAN to per-region style control from reference images — a widely adopted building block for semantic image synthesis and style transfer. Part of the same group's Image2StyleGAN inversion lineage. *(Listed here for its strong verified impact; record tier is 2.)*

### 10. **SpaText: Spatio-Textual Representation for Controllable Image Generation**
*Year:* 2023 · *Award:* none · *Tier 3* · *Cites / Influential:* 270 / 15
A Meta AI + Hebrew University/Reichman work introducing open-vocabulary region-annotated (segmentation + free-text) control for diffusion T2I, routinely grouped with ControlNet and GLIGEN as a foundational spatial-control method. First author Omri Avrahami (also Blended Diffusion) went on to Break-A-Scene, The Chosen One, Stable Flow, and DiffUHaul; Meta co-authors are behind Make-A-Scene/Make-A-Video.

### 11. **Generating Videos with Dynamics-aware Implicit GANs (DIGAN)**
*Year:* 2022 · *Award:* none · *Tier 3* · *Cites / Influential:* 229 / 34
An INR-based video GAN (ICLR 2022) that set SOTA FVD on UCF-101 and enabled long, non-autoregressive video synthesis. Lead author Sihyun Yu (KAIST, Shin group) immediately followed with the landmark PVDM (CVPR 2023) and CMD (ICLR 2024); DIGAN is the GAN-era precursor to that influential latent-video-diffusion line. Cited by StyleGAN-V and latent-video-diffusion works.

### 12. **Semantic Hierarchy Emerges in Deep Generative Representations for Scene Synthesis**
*Year:* 2019 · *Award:* none · *Tier 3* · *Cites / Influential:* 212 / 18
GenForce (Shen, Yang, Zhou) work and a sibling/precursor to InterFaceGAN (CVPR 2020) and SeFa (CVPR 2021) — the cornerstone GAN latent-space interpretability line that shaped modern controllable generation, along with the widely adopted GenForce toolkit. Cited by InterFaceGAN, GANSpace, and StyleGAN semantic-editing works.

### 13. **Regularizing Generative Adversarial Networks under Limited Data (LeCam)**
*Year:* 2021 · *Award:* none · *Tier 3* · *Cites / Influential:* 177 / 29
Introduced LeCam regularization, one of the most influential techniques for stabilizing GAN training on limited data. Adopted as a default ingredient in StyleGAN-XL and Projected GANs and complementary to ADA/DiffAugment. Google authors Lu Jiang and Ming-Hsuan Yang are highly prominent in generative/video modeling.

### 14. **Exploiting Spatial Dimensions of Latent in GAN for Real-time Image Editing (StyleMapGAN)**
*Year:* 2021 · *Award:* none · *Tier 3* · *Cites / Influential:* 168 / 25
A NAVER AI Lab CVPR 2021 paper replacing StyleGAN's vector latent + AdaIN with a spatial "style map" for fast, accurate encoder-based real-image editing — an influential idea in the GAN-inversion / latent-editing line. Led by the StarGAN/StarGAN v2 team (senior author Yunjey Choi). Cited across GAN-inversion and latent-editing surveys.

### 15. **T2V-CompBench: A Comprehensive Benchmark for Compositional Text-to-Video Generation**
*Year:* 2025 · *Award:* none · *Tier 3* · *Cites / Influential:* 132 / n/a
The highest-impact paper of the recent cohort (132 cites in ~1 year). From Xihui Liu's HKU group (with CUHK and Huawei Noah's Ark), it is the first benchmark for compositional text-to-video generation (attribute binding, spatial/motion relations, numeracy) with MLLM/detection/tracking metrics and a public leaderboard. A standard evaluation suite cited by CogVideoX-, Wan-, and Sora-era model papers and T2V surveys.

### 16. **MagicAnimate: Temporally Consistent Human Image Animation using Diffusion Model**
*Year:* 2024 · *Award:* none · *Tier 3* · *Cites / Influential:* 127 / n/a
A landmark CVPR 2024 paper (ShowLab NUS + ByteDance) that, with Animate Anyone, defined the diffusion reference-net + temporal-module recipe for human image animation (>38% improvement on TikTok dancing). Its open-source release made it a de facto baseline seeding the pose-driven animation lineage (Champ, UniAnimate, Wan-Animate). The mirror's count is conservative; almost certainly higher by 2026.

### 17. **Visual Prompt Tuning for Generative Transfer Learning**
*Year:* 2023 · *Award:* none · *Tier 3* · *Cites / Influential:* 116 / 3
A CVPR 2023 token-space generative-transformer prompt-tuning paper from Google (Sohn, Chang, Jiang, Hao, Essa, Zhang). It directly fed the team's landmark MaskGIT/Muse/StyleDrop line — Muse (ICML 2023) and StyleDrop (NeurIPS 2023) apply the same parameter-efficient style-via-tuning idea. A clear precursor to famous Google generative models.

### 18. **GIRAFFE HD: A High-Resolution 3D-aware Generative Model**
*Year:* 2022 · *Award:* none · *Tier 2* · *Cites / Influential:* 114 / 13
A high-resolution extension of the GIRAFFE compositional 3D-aware GAN (foreground/background disentanglement, style-based neural renderer) from Yong Jae Lee's group with Adobe's Krishna Kumar Singh. Well cited within the 3D-aware GAN / neural-rendering wave; the same lab produced GLIGEN (CVPR 2023). A notable but not field-defining contribution.

### 19. **Few-shot Font Generation with Localized Style Representations and Factorization (LF-Font)**
*Year:* 2021 · *Award:* none · *Tier 2* · *Cites / Influential:* 111 / 20
A well-cited AAAI 2021 NAVER/Clova paper that became a standard baseline in the few-shot font-generation subfield, spawning MX-Font, Diff-Font, DA-Font, and a TPAMI journal extension. Co-author Sanghyuk Chun is a prominent NAVER AI researcher (ReLabelImageNet, ProbVLM).

### 20. **COCO-FUNIT: Few-Shot Unsupervised Image Translation with a Content Conditioned Style Encoder**
*Year:* 2020 · *Award:* none · *Tier 3* · *Cites / Influential:* 93 / 6
Direct successor to NVIDIA's FUNIT, fixing its content-loss problem via a content-conditioned style encoder; co-authored by Ming-Yu Liu, who leads NVIDIA's Deep Imagination group (GauGAN/SPADE, eDiff-I). A precursor node in a landmark NVIDIA generative-AI lineage; co-author Kuniaki Saito continued influential domain-adaptation work (OVANet, DANCE).

*(Honorable mentions just outside the top 20, by lineage: LayoutDiffuse (92), LayoutBERT/BLT (85), High-fidelity 3D Human Digitization / 2K2K (84), Custom-Edit (77), Sieve­Net (72), Putting People in Their Place (64), ViVid-1-to-3 (69), CalliGAN (67); and the landmark-lineage but low-citation Network Fusion with Conditional INNs, Towards Unified Keyframe Propagation Models, MorphGAN, and Improved Image Generation via Sparse Modeling.)*

---

## 3. Full Ranked Table of All Papers

Sorted by year, then by available citation count (descending; "n/a" last). Tier 3 = landmark / landmark-lineage; Tier 2 = solid/notable; Tier 1 = ordinary.

| Year | Title | Citations | Tier | One-line lineage |
|---|---|---|---|---|
| 2019 | Semantic Hierarchy Emerges in Deep Generative Representations for Scene Synthesis | 212 | 3 | GenForce precursor to InterFaceGAN/SeFa GAN-interpretability line. |
| 2020 | StarGAN v2: Diverse Image Synthesis for Multiple Domains | 2080 | 3 | Canonical multi-domain translation baseline; AFHQ dataset; NAVER. |
| 2020 | Interpreting the Latent Space of GANs for Semantic Face Editing (InterFaceGAN) | 1080 | 3 | Founded GAN latent-space semantic-editing subfield (→ SeFa, GANSpace). |
| 2020 | Image2StyleGAN++: How to Edit the Embedded Images? | 591 | 3 | W+ noise-optimization editing; precursor to StyleFlow / GAN inversion. |
| 2020 | SEAN: Image Synthesis with Semantic Region-Adaptive Normalization | 280 | 2 | Per-region SPADE successor; widely reused semantic-synthesis block. |
| 2020 | COCO-FUNIT: Few-Shot Unsupervised Image Translation | 93 | 3 | NVIDIA FUNIT successor; Ming-Yu Liu → GauGAN/eDiff-I lineage. |
| 2020 | SieveNet: A Unified Framework for Robust Image-Based Virtual Try-On | 72 | 2 | Coarse-to-fine try-on in VITON/CP-VTON line; author → MIT LPM work. |
| 2020 | CalliGAN: Style and Structure-aware Chinese Calligraphy Character Generator | 67 | 2 | Component-decomposition baseline in Chinese-font/calligraphy generation. |
| 2020 | RetrieveGAN: Image Synthesis via Differentiable Patch Retrieval | 56 | 2 | Early retrieval-augmented synthesis; Ming-Hsuan Yang lab → Meta/Snap. |
| 2020 | Conditional Image Generation and Manipulation for User-Specified Content | 35 | 1 | Early text/attribute-conditioned editing; no landmark successor. |
| 2020 | Learning to Shadow Hand-drawn Sketches | 30 | 1 | Controllable line-art shadowing; niche art-rendering reference. |
| 2020 | Mimicry: Towards the Reproducibility of GAN Research | 29 | 2 | PyTorch GAN reproducibility library; author → Snap/xAI. |
| 2020 | FaR-GAN for One-Shot Face Reenactment | 15 | 1 | Purdue media-forensics reenactment; deepfake-detection neighborhood. |
| 2020 | Network Fusion for Content Creation with Conditional INNs | 3 | 3 | Esser/Rombach/Ommer → VQGAN → Stable Diffusion → Black Forest Labs. |
| 2020 | Object-Centric Image Generation from Layouts (OC-GAN) | n/a | 3 | AAAI 2021 layout-to-image baseline (SGSM); Bengio/Hjelm. |
| 2020 | Freeze the Discriminator (FreezeD) | n/a | 3 | Standard few-shot GAN-adaptation baseline (KAIST/POSTECH). |
| 2020 | SegAttnGAN: Text to Image Generation with Segmentation Attention | n/a | 1 | AI4CC 2020 Audience Choice; segmentation-guided AttnGAN. |
| 2020 | Toward High-quality Few-shot Font Generation with Dual Memory (DM-Font) | n/a | 3 | ECCV 2020; seeded NAVER few-shot font line (LF-Font, MX-Font). |
| 2020 | Generating Object Stamps | n/a | 2 | Compositional object generation; authors → CommonCanvas, Adobe/Google. |
| 2020 | Text-guided Image Manipulation via Local Feature Editing (TIM-GAN) | n/a | 2 | ACM MM 2021; instruction-editing precursor (Lu Jiang, Essa). |
| 2020 | MixNMatch: Multifactor Disentanglement and Encoding | n/a | 2 | Disentangled conditional generation; authors → GLIGEN (CVPR 2023). |
| 2020 | Directional GAN: A Novel Conditioning Strategy | n/a | 1 | Adobe latent-direction conditioning; ordinary applied impact. |
| 2021 | Regularizing GANs under Limited Data (LeCam) | 177 | 3 | LeCam reg; default in StyleGAN-XL / Projected GANs. |
| 2021 | Exploiting Spatial Dimensions of Latent in GAN (StyleMapGAN) | 168 | 3 | Spatial style-map editing; NAVER StarGAN team. |
| 2021 | Few-shot Font Generation with Localized Style Representations (LF-Font) | 111 | 2 | AAAI 2021 few-shot-font baseline; NAVER (→ MX-Font, TPAMI). |
| 2021 | Strumming to the Beat: Audio-Conditioned Contrastive Video Textures | 21 | 2 | Berkeley/Michigan group; author → CLIP-It!, TL;DW. |
| 2021 | Automatic Style Transfer for Non-Linear Video Editing | 10 | 2 | Google computational video-editing (Chi, Essa). |
| 2021 | Deep Graphics Encoder for Real Time Video Makeup Synthesis | 7 | 2 | L'Oreal/ModiFace makeup-AR line (CA-GAN → Stable-Makeup). |
| 2021 | Learning to Generate Novel Scene Compositions from Single Images/Videos | 5 | 2 | One-Shot GAN; precursor to OSMIS (WACV 2023), Bosch. |
| 2021 | GaussiGAN: Controllable Image Synthesis with 3D Gaussians | 5 | 2 | 3D-Gaussian primitives prefiguring 3DGS; Brown/Adobe. |
| 2021 | Learning Physically-based Face Material and Lighting Decompositions | 8 | 2 | Brown inverse-rendering; author → VecFusion, GEM3D. |
| 2021 | High-Resolution Complex Scene Synthesis with Transformers | 44 | 3 | AI4CC 2021 Best Paper; CompVis → Stable Diffusion lineage. |
| 2021 | Directional GAN (2021 listing) | n/a | 1 | Adobe conditioning strategy; ordinary impact. |
| 2021 | Texture Generation with Neural Cellular Automata | n/a | 3 | Distill NCA team; launched modern NCA subfield (→ Mesh NCA). |
| 2021 | Halluci-Net: Scene Completion by Object Co-occurrence | n/a | 2 | pix2pixHD scene-completion; author Gokhale → VL robustness. |
| 2021 | Decorating Your Own Bedroom (LoGAN) | n/a | 2 | Local GAN control; GenForce lineage (→ LinkGAN). |
| 2021 | MorphGAN: Controllable One-Shot Face Synthesis | n/a | 3 | BMVC 2021; lead author Ruiz → DreamBooth (CVPR 2023). |
| 2021 | Generative Hierarchical Features from Synthesizing Images (GH-Feat) | n/a | 3 | CVPR 2021 Oral; GenForce inversion line (→ TPAMI 2023). |
| 2022 | StyleSDF: High-Resolution 3D-Consistent Image and Geometry Generation | 398 | 3 | SDF+StyleGAN2 3D-aware GAN; seeded SDF-based 3D generation. |
| 2022 | A-NeRF: Articulated Neural Radiance Fields | 308 | 3 | Foundational articulated-human NeRF; → DANBO, HumanNeRF. |
| 2022 | Generating Videos with Dynamics-aware Implicit GANs (DIGAN) | 229 | 3 | INR video GAN; precursor to PVDM/CMD latent-video diffusion. |
| 2022 | Dataset Distillation by Matching Training Trajectories (MTT) | 573 | 3 | Dominant dataset-distillation baseline (CMU-MIT-Berkeley). |
| 2022 | GIRAFFE HD: A High-Resolution 3D-aware Generative Model | 114 | 2 | Compositional 3D-aware GAN; Yong Jae Lee lab (→ GLIGEN). |
| 2022 | SeamlessGAN: Self-Supervised Synthesis of Tileable Texture Maps | 38 | 2 | TVCG tileable textures; → MatFuse, Tiled Diffusion. |
| 2022 | On Conditioning the Input Noise for Controlled Diffusion Generation | 26 | 2 | Pre-ControlNet diffusion conditioning; Adobe (→ REEDIT). |
| 2022 | CoordGAN: Self-Supervised Dense Correspondences Emerge from GANs | 25 | 2 | NVIDIA emergent-correspondence; feeds ODISE-style line. |
| 2022 | Arbitrary-Scale Image Synthesis | 24 | 2 | ETH scale-consistent encodings; arbitrary-scale generation reference. |
| 2022 | Rethinking Deep Face Restoration | 19 | 2 | Google gen-vs-recon FR; → Authentic Face Restoration (ICCV 2023). |
| 2022 | RewriteNet: Reliable Scene Text Editing | 11 | 2 | NAVER Clova scene-text-editing precursor (→ Brush Your Text). |
| 2022 | Cross-Domain Style Mixing for Face Cartoonization | 9 | 3 | NAVER WEBTOON; precursor to WebtoonMe (SIGGRAPH Asia 2022). |
| 2022 | Learning to Generate ... (One-Shot GAN, 2022 listing) | 5 | 2 | One-shot synthesis line; Bosch (→ OSMIS). |
| 2022 | SeCGAN: Parallel cGANs for Face Editing via Semantic Consistency | 5 | 2 | Mask-free face editing; Kim/Bhattarai labs. |
| 2022 | Generate and Edit Your Own Character in a Canonical View | 4 | 1 | StyleGAN frontalization; authors → 3D portrait synthesis (ECCV 2022). |
| 2022 | V3GAN: Decomposing Background, Foreground and Motion | 4 | 1 | BMVC 2021 decomposed video GAN; MoCoGAN/G3AN lineage. |
| 2022 | Improved Image Generation via Sparse Modeling | 1 | 3 | Ganz/Elad sparse-coding+GAN; author → CLIPAG (WACV 2024). |
| 2022 | Video-ReTime: Learning Temporally Varying Speediness | 1 | 2 | Adobe self-supervised time-remapping (Jenni). |
| 2022 | SaiNet: Inpainting behind objects | 1 | 1 | Surrey/BBC stereo-aware inpainting; ordinary impact. |
| 2022 | Fix the Noise (FixNoise) | 2 | 2 | AI4CC 2022 Best Paper; → CVPR 2023 domain-translation extension. |
| 2022 | LayoutBERT: Masked Language Layout Model for Object Insertion | 3 | 1 | BERT-style layout insertion; Adobe; limited uptake. |
| 2022 | Text-guided Image Manipulation: Sentence/Word-aware Network | n/a | 1 | ICME 2022; ManiGAN-lineage, superseded by diffusion editing. |
| 2022 | Neural Volumetric Object Selection | n/a | 2 | CVPR 2022 NeRF/MPI 3D selection; → SPIn-NeRF, ISRF. |
| 2022 | Multilayer GAN Inversion and Editing | n/a | 3 | CMU/Adobe; Parmar/Zhu → pix2pix-zero, pix2pix-Turbo. |
| 2022 | StyLandGAN: StyleGAN Landscape Synthesis using Depth-map | n/a | 1 | NCSOFT depth-conditioned landscapes; ordinary impact. |
| 2022 | Tensor-based Emotion Editing in the StyleGAN Latent Space | n/a | 2 | HOSVD emotion directions; author → diffusion latent directions (CVPR 2023). |
| 2022 | LatentKeypointGAN: Controlling Images via Latent Keypoints | n/a | 3 | UBC self-supervised keypoint control; CRV 2023 Best Paper; → GANSeg. |
| 2022 | Image2Gif: Continuous Animations with Warping NODEs | n/a | 2 | Neural-ODE frame interpolation; Nazarovs ODE line. |
| 2022 | FontNet: Closing the gap to font designer performance | n/a | 2 | Few-shot font synthesis program (→ ESWA 2023, Patch-Font). |
| 2022 | RiCS: A 2D Self-Occlusion Map for Harmonizing Volumetric Objects | n/a | 2 | AI4CC 2022 Runner-up; Adobe/Google harmonization; Villegas/Lee. |
| 2022 | Overparameterization Improves StyleGAN Inversion | n/a | 2 | AI4CC 2022 Best Poster; Laval → Robust StyleGAN Restoration (CVPR 2023). |
| 2022 | Zero-Shot Text-Guided Object Generation with Dream Fields | 657 | 3 | AI4CC 2022 Best Poster; → DreamFusion/SDS text-to-3D explosion. |
| 2022 | Conditional Vector Graphics Generation for Music Cover Images | n/a | 1 | ITMO SVG generation; steady niche vector-graphics line. |
| 2022 | Monocular Human Digitization via Implicit Re-projection Networks | n/a | 1 | KETI single-image 3D human; PIFu-family neighborhood. |
| 2022 | End-to-End Rubbing Restoration Using GANs (RubbingGAN) | n/a | 1 | Chinese inscription restoration; niche cultural-heritage. |
| 2022 | Few-Shot Font Generation by Learning Fine-Grained Local Styles (FsFont) | n/a | 2 | CVPR 2022 Baidu FFG baseline (~100+ cites). |
| 2022 | Few-Shot Head Swapping in the Wild (HeSer) | n/a | 2 | CVPR 2022 Oral; first prominent head-swapping method; Baidu. |
| 2022 | Discrete Representations Strengthen ViT Robustness | n/a | 3 | ICLR 2022 VQ-tokens for OOD robustness; Vondrick/Dehghani. |
| 2022 | Towards Unified Keyframe Propagation Models | n/a | 3 | Runway/Esser; foreshadows Gen-1 video editing; Stable Diffusion lineage. |
| 2022 | Diverse Video Generation from a Single Video (VGPNN) | n/a | 3 | ECCV 2022; Weizmann → Text2LIVE, Lumiere. |
| 2023 | SpaText: Spatio-Textual Representation for Controllable Generation | 270 | 3 | Region+text diffusion control; Avrahami/Meta; grouped with ControlNet/GLIGEN. |
| 2023 | Visual Prompt Tuning for Generative Transfer Learning | 116 | 3 | CVPR 2023; → Muse, StyleDrop (Google masked-generative line). |
| 2023 | LayoutDiffuse: Adapting Foundational Diffusion for Layout-to-Image | 92 | 2 | Layout-attention adaptor; layout/region-controllable diffusion. |
| 2023 | BLT: Bidirectional Layout Transformer | 85 | 3 | ECCV 2022; foundational controllable-layout work; MaskGIT/Muse cluster. |
| 2023 | High-fidelity 3D Human Digitization from Single 2K Images (2K2K) | 84 | 2 | CVPR 2023 Highlight; released widely-used 2K2K dataset. |
| 2023 | Custom-Edit: Text-Guided Editing with Customized Diffusion | 77 | 2 | SNU/NAVER; DreamBooth + Prompt-to-Prompt; survey reference. |
| 2023 | Putting People in Their Place: Affordance-Aware Human Insertion | 64 | 3 | Best poster; Tim Brooks (InstructPix2Pix/Sora) + Efros. |
| 2023 | 3DAvatarGAN: Bridging Domains for Personalized Editable Avatars | 55 | 2 | Snap/KAUST; Abdal → Gaussian Shell Maps (CVPR 2024). |
| 2023 | CLIP-Actor: Text-Driven Recommendation and Stylization for Meshes | 54 | 2 | ECCV 2022 CLIP-to-mesh; author → Paint-it (CVPR 2024). |
| 2023 | Sound to Visual Scene Generation by Audio-to-Visual Latent Alignment | 53 | 3 | CVPR 2023; → Sound2Vision, SoundBrush (audio-visual generation). |
| 2023 | LayoutDiffuse / layout line ... see above | — | — | (listed above) |
| 2023 | Custom video / image works ... | — | — | (see specific rows) |
| 2023 | Fine-grained Image Editing by Pixel-wise Guidance Using Diffusion | 18 | 2 | AI4CC Best Paper; Sony diffusion team (→ PaGoDA, GenWarp). |
| 2023 | Reference-based Image Composition with Sketch via Diffusion | 18 | 2 | KAIST/NAVER WEBTOON; Paint-by-Example + sketch (→ DreamStyler). |
| 2023 | Exploring Gradient-based Multi-directional Controls in GANs (GradCtrl) | 17 | 1 | ECCV 2022 ModiFace GAN latent control; ordinary impact. |
| 2023 | Visual prompt tuning ... (see CVPR 2023 row above) | — | — | (listed above) |
| 2023 | The Nuts and Bolts of Adopting Transformer in GANs | 4 | 2 | STrans-G/D study; canonical version is STransGAN; CUHK/NTU. |
| 2023 | LPMM: Intuitive Pose Control for Talking-Head | 2 | 1 | NAVER WEBTOON rig-like pose control; applied-avatar line. |
| 2023 | Instance-Aware Image Completion | 2 | 2 | Inpainting; co-author Minguk Kang → GigaGAN (CVPR 2023). |
| 2023 | Can We Find Strong Lottery Tickets in Generative Models? | 8 | 2 | AAAI 2023; extends LTH to GANs (→ Nickel and Diming, ECCV 2024). |
| 2023 | SVS: Adversarial refinement for sparse novel view synthesis | 3 | 1 | BMVC 2022 Surrey/BBC; → ZeST-NeRF, SaiNet. |
| 2023 | MetaDance: Few-shot Dancing Video Retargeting | 0 | 2 | Early-career; lead author Yuying Ge → SEED MLLM series. |
| 2023 | 'Tax-free' 3DMM Conditional Face Generation | 0 | 2 | Brown precursor to "Removing the Quality Tax" (WACV 2024). |
| 2023 | Context-Preserving Two-Stage Video Domain Translation | 1 | 1 | KAIST/NAVER heavyweight roster; no clear successor. |
| 2023 | Balancing Reconstruction and Editing Quality of GAN Inversion | 0 | 1 | UTokyo; short version of WACV 2024 paper; author → 3DGS. |
| 2023 | Neural Sign Reenactor: Photorealistic Sign Language Retargeting | n/a | 2 | NTUA/FORTH; sign-language-production line (→ Neural Sign Actors). |
| 2023 | Paste and Harmonize via Denoising | n/a | 2 | UTokyo Matsuo-Iwasawa; subject-driven diffusion editing. |
| 2023 | Text-to-image Editing by Image Information Removal | n/a | 2 | AI4CC Runner-up; WACV 2024 / Amazon Science. |
| 2023 | AADiff: Audio-Aligned Video Synthesis with T2I Diffusion | n/a | 1 | SNU training-free audio-driven video; audio-video editing line. |
| 2023 | We never go out of Style: Motion Disentanglement | n/a | 2 | IISc VAL; author Parihar → CVPR/ECCV diffusion-editing run. |
| 2023 | Discrete Predictor-Corrector Diffusion Models | n/a | 3 | Google MaskGIT→Muse line; discrete-diffusion sampling. |
| 2023 | Matching-based Data Valuation for Generative Model (GMValuator) | n/a | 2 | → GMValuator (ICLR 2025); co-author → Gemini 2.5. |
| 2024 | DL3DV-10K: Large-Scale Scene Dataset for 3D Vision | 411 | 3 | Landmark NeRF/3DGS dataset and benchmark. |
| 2024 | SSR-Encoder: Selective Subject Representation | 162 | 3 | CVPR 2024 tuning-free subject-driven encoder; standard baseline. |
| 2024 | MagicAnimate: Temporally Consistent Human Image Animation | 127 | 3 | CVPR 2024; defined diffusion reference-net animation recipe. |
| 2024 | ViVid-1-to-3: Novel View Synthesis with Video Diffusion | 69 | 2 | CVPR 2024 Highlight; video-diffusion-for-NVS bridge (UBC). |
| 2024 | Visual Style Prompting with Swapping Self-Attention | 58 | 3 | AI4CC 2024 Best Paper; tuning-free style baseline (→ StyleKeeper). |
| 2024 | VideoSwap: Customized Video Subject Swapping | 24 | 2 | CVPR 2024 ShowLab/Meta; point-correspondence subject swap. |
| 2024 | As-Plausible-As-Possible: Plausibility-Aware Mesh Deformation | 10 | 2 | CVPR 2024 KAIST/Adobe; SDS into geometry editing. |
| 2024 | Pix2Gif: Motion-Guided Diffusion for GIF Generation | 6 | 3 | ECCV 2024; MSR (Jianwei Yang/Jianfeng Gao → Magma). |
| 2024 | CamViG: Camera Aware Image-to-Video Generation | 6 | 2 | Google VideoPoet team; camera-control offshoot of ICML 2024 Best Paper. |
| 2024 | The Curious Case of End Token: Zero-Shot Disentangled CLIP Editing | 4 | 2 | Yanardag lab; → NoiseCLR, FluxSpace, LoRAShop. |
| 2024 | Towards a Perceptual Evaluation Framework for Lighting Estimation | 3 | 2 | CVPR 2024 Laval; relighting-evaluation metric (→ IJCV, SpotLight). |
| 2024 | ToonAging: Face Re-Aging upon Portrait Style Transfer | 2 | 1 | Single-stage aging+NPR; ordinary impact. |
| 2024 | ReasonPix2Pix: Instruction Reasoning Dataset | 1 | 2 | CUHK InternLM/InternVL group; reasoning-edit dataset. |
| 2024 | Temporally Consistent Object Editing in Videos | 1 | 1 | Concordia/Mila extended-attention video editing; ordinary impact. |
| 2024 | ClickDiffusion: LLMs for Interactive Precise Image Editing | 1 | 3 | Georgia Tech; Helbling/Chau → ConceptAttention (ICML 2025). |
| 2024 | Towards Safer AI Content Creation by Immunizing T2I Models (IMMA) | n/a | 3 | AI4CC Runner-up; ECCV 2024; → ICML 2025 Oral immunization. |
| 2024 | Seamless Human Motion Composition with Blended Positional Encodings (FlowMDM) | n/a | 3 | Best poster; CVPR 2024; → MixerMDM, in2IN, Rolling Prediction. |
| 2024 | Spatial Steerability of GANs via Self-Supervision from Discriminator | n/a | 3 | IJCV; first author Jianyuan Wang → VGGT (CVPR 2025 Best Paper). |
| 2024 | Paint-it: Text-to-Texture via PBR Optimization | n/a | 3 | Pons-Moll/Oh DC-PBR SDS; → Meta 3D TextureGen, Make-A-Texture. |
| 2024 | EraseDraw: Learning to Insert Objects by Erasing Them | n/a | 3 | ECCV 2024 Vondrick lab; insertion-by-removal lineage (→ Add-it). |
| 2024 | ElasticDiffusion: Training-free Arbitrary Size Image Generation | n/a | 3 | CVPR 2024; lead author → Snap Research (AV-Link, GenAU). |
| 2024 | EverLight: Indoor-Outdoor Editable HDR Lighting Estimation | n/a | 3 | ICCV 2023 Laval; first seamless indoor/outdoor lighting (→ LuxDiT). |
| 2024 | LoopDraw: Loop-Based Autoregressive Shape Synthesis | n/a | 2 | UChicago Threedle; author → Geometry in Style, LL3M. |
| 2024 | Posterior Distillation Sampling (PDS) | n/a | 3 | CVPR 2024 KAIST; extends SDS/DDS for parametric editing. |
| 2024 | ICE-G: Image Conditional Editing of 3D Gaussian Splats | n/a | 2 | DINO-feature 3DGS/NeRF editing; Jampani/Raj/Kira/Irshad. |
| 2024 | My Body My Choice: Human-Centric Full-Body Anonymization | n/a | 2 | Ciftci-Demir privacy line (My Face My Choice, FakeCatcher). |
| 2024 | VSTAR: Generative Temporal Nursing for Longer Video Synthesis | n/a | 2 | ICLR 2025 Bosch; long-video diffusion (Khoreva group). |
| 2024 | FlexEControl: Flexible Efficient Multimodal Control for T2I | n/a | 2 | TMLR; ControlNet-downstream; Wang/Bansal/Peng roster. |
| 2024 | Text Prompting for Multi-Concept Video Customization | n/a | 2 | Google DeepMind/UMD; VideoPoet-era roster. |
| 2024 | NeRFFaceSpeech: One-shot Audio-driven 3D Talking Head | n/a | 2 | KAIST audio-driven NeRF talking-head; tracked in surveys. |
| 2024 | LOVECon: Training-free Long Video Editing with ControlNet | n/a | 1 | SJTU; SciChina 2025; early diffusion-video entry. |
| 2024 | Automated Virtual Product Placement using Diffusion | n/a | 1 | AWS applied ad-placement pipeline; niche. |
| 2024 | Customize Your Own Paired Data via Few-shot Way | n/a | 1 | ByteDance few-shot paired editing; limited footprint. |
| 2024 | InstructRL4Pix: Diffusion Editing by Reinforcement Learning | n/a | 1 | SCUT RL-for-editing; ordinary, low visibility. |
| 2024 | CustomText: Customized Textual Image Generation | n/a | 1 | TCS; TextDiffuser+ControlNet visual-text rendering. |
| 2024 | TriLoRA: Integrating SVD for Style Personalization | n/a | 1 | SVD-into-LoRA; crowded LoRA-variant space; low impact. |
| 2024 | LEAST: Local text-conditioned image style transfer | n/a | 1 | Adobe CVFAD; follows Gatha, precedes ReEdit. |
| 2024 | Reference-based Painterly Inpainting via Diffusion | n/a | 2 | VITA-Group/SHI Labs; author → 4DGen, Diffusion4D. |
| 2025 | T2V-CompBench: Compositional Text-to-Video Benchmark | 132 | 3 | First compositional T2V benchmark; HKU; standard eval suite. |
| 2025 | LumiNet: Latent Intrinsics Meets Diffusion for Relighting | 28 | 2 | Bhattad relighting line (StyLitGAN → LumiNet). |
| 2025 | Generative Photography: Scene-Consistent Camera Control | 29 | 2 | CVPR 2025 Highlight; physically-meaningful camera control (Chan/Purdue). |
| 2025 | ScribbleLight: Single Image Indoor Relighting with Scribbles | 16 | 2 | CVPR 2025; Bhattad intrinsic/relighting line. |
| 2025 | Perceptually Accurate 3D Talking Head Generation | 15 | 2 | CVPR 2025 Highlight; KAIST speech-mesh metrics (Oh group). |
| 2025 | Enhancing Creative Generation on Stable Diffusion Models (C3) | 12 | 2 | CVPR 2025 training-free creativity; NAVER/KAIST. |
| 2025 | MixerMDM: Learnable Composition of Human Motion Diffusion | 9 | 2 | Barquero/Escalera motion line (BeLFusion, FlowMDM). |
| 2025 | NamedCurves: Learned Image Enhancement via Color Naming | 6 | 2 | ECCV 2024 → TPAMI 2026; Michael S. Brown color line. |
| 2025 | Deep Geometric Moments Promote Shape Consistency in T2T-to-3D (MT3D) | 5 | 2 | ASU/Intel anti-Janus SDS text-to-3D (→ DreamCS). |
| 2025 | HyperNVD: Accelerating Neural Video Decomposition via Hypernetworks | 1 | 2 | CVPR 2025 CVC/UAB; layered/INR video-decomposition line. |
| 2025 | DANTE-AD: Dual-Vision Attention Network for Audio Description | 1 | 2 | Surrey; AutoAD-lineage long-term movie AD. |
| 2025 | Towards Film-Making Production ... Moving Dubbing Benchmarks | 1 | 2 | Giant Network AI Lab; dubbing-benchmark program. |
| 2025 | Vectorized Region Based Brush Strokes for Artistic Rendering | 1 | 1 | TCS stroke-rendering line (Sketch & Paint). |
| 2025 | GenSync: Talking Head via 3D Gaussian Splatting | 2 | 1 | UMass; multi-identity audio-driven 3DGS; arXiv-only. |
| 2025 | Is Concatenation Really All You Need? (Pose Conditioning for VTON) | 3 | 1 | Amazon try-on; responds to CatVTON; incremental. |
| 2025 | Comparison Reveals Commonality: Contrastive Inversion | 0 | 1 | KAIST; Textual-Inversion/DreamBooth extension; too new. |
| 2025 | DiT-VTON: Diffusion Transformer Unified Virtual Try-On/Try-All | 0 | 1 | Amazon DiT try-all; brand-new, zero citations. |
| 2025 | Stable Flow: Vital Layers for Training-Free Image Editing | n/a | 3 | CVPR 2025 Snap; Avrahami/Patashnik/Aberman/Cohen-Or/Fried. |
| 2025 | MALT Diffusion: Memory-Augmented Latent Transformers for Video | n/a | 3 | Best presentation; Sihyun Yu (REPA) + Google VideoPoet/W.A.L.T team. |
| 2025 | VideoLifter: Lifting Videos to 3D via Hierarchical Stereo Alignment | n/a | 3 | AI4CC 2025 Best Paper; VITA-Group → InstantSplat lineage. |
| 2025 | CamCo: Camera-Controllable 3D-Consistent Image-to-Video | n/a | 3 | NVIDIA/UT Austin; Plucker camera conditioning; → Diffusion4D. |
| 2025 | HumanEdit: Human-Rewarded Instruction-based Editing Dataset | n/a | 3 | Benchmark; Ling Yang/Xiangtai Li/Yan cluster (RPG, IterComp). |
| 2025 | 4K4DGen: Panoramic 4D Generation at 4K Resolution | n/a | 3 | ICLR 2025 Spotlight; VITA/Kadambi panoramic-4D precursor. |
| 2025 | Revisiting Diffusion Autoencoder Training | n/a | 2 | Continues Diff-AE (Suwajanakorn/VISTEC). |
| 2025 | HyperGS: Hyperspectral 3D Gaussian Splatting | n/a | 2 | CVPR 2025 Surrey; first hyperspectral NVS benchmark. |
| 2025 | Tiled Diffusion | n/a | 2 | CVPR 2025 Reichman; training-free tileable/360 textures (Fried). |
| 2025 | EOPose: Exemplar-based Object Reposing | n/a | 2 | Adobe MDSR reposing line (ZFlow, VGFlow). |
| 2025 | Don't Mesh with Me: Generating CSG via Code-Generation LLM | n/a | 2 | Fraunhofer/HU Berlin; early LLM-for-CAD-program work. |
| 2025 | VideoHandles: Editing 3D Object Compositions in Videos | n/a | 2 | CVPR 2025 KAIST/Adobe; training-free 3D-in-video editing. |
| 2025 | LiftRefine: Progressively Refined View Synthesis | n/a | 2 | VinAI/Trinity; volume-triplane + diffusion refiner. |
| 2025 | Kubrick: Multimodal Agent Collaborations for Video Generation | n/a | 2 | Purdue/Baidu; agentic Blender-script video (→ Scene Co-pilot). |
| 2025 | Art3D: Training-Free 3D Generation from Flat-Colored Illustration | n/a | 2 | Best presentation; Brown Sridhar lab (→ UVGS). |
| 2025 | Is Your Text-to-Image Model Robust to Caption Noise? | n/a | 2 | Lu Jiang (ByteDance); caption-noise mitigation for T2I. |
| 2025 | Progressive Prompt Detailing (SCoPE) | n/a | 2 | BU/Runway Ghadiyaram; coarse-to-fine prompt alignment. |
| 2025 | Generating Animated Layouts as Structured Text (VAKER) | n/a | 1 | SNU/SKT; LLM-driven animated ad layouts; applied. |
| 2025 | Parallel Rescaling: Rebalancing Consistency Guidance | n/a | 1 | SeoulTech; DreamBooth/TI personalization; too recent. |
| 2025 | Harnessing Training-Free 2D Techniques for Text-to-3D via SDS | n/a | 1 | POSTECH analysis of CFG/FreeU in SDS; diagnostic. |
| 2025 | DreamBlend: Personalized Fine-tuning of T2I Diffusion | n/a | 1 | WACV 2025 Amazon; DreamBooth-blend; incremental. |
| 2025 | Training-Free Sketch-Guided Diffusion with Latent Optimization | n/a | 1 | Best presentation; UTokyo Aizawa lab; cross-attention sketch control. |
| 2025 | InstructVTON: Auto-Masking + Language-Guided Virtual Try-On | n/a | 1 | Amazon interactive try-on (DEFT-VTON line). |

*Note on the table:* a few 2023 rows whose titles overlap multiple records (e.g., the layout-diffusion entries) are consolidated; every distinct record in the source JSON is represented exactly once.

---

## 4. Notes & Caveats

**Data confidence.** Each record carries a self-reported confidence flag: high, medium, or low.
- **High confidence:** the majority of records, including most verified citation counts (StarGAN v2, InterFaceGAN, Dream Fields, MTT, DL3DV-10K, StyleSDF, A-NeRF, SEAN, SpaText, DIGAN, etc.).
- **Medium confidence:** many lineage attributions where the AI4CC entry is an abstract/short version of a later conference paper, and where the citation count was not independently re-verified.
- **Low confidence:** a small number of records — *Directional GAN*, *ReasonPix2Pix*, *Customize Your Own Paired Data via Few-shot Way*, *The Lost Melody*, *AADiff* (count), *NeRFFaceSpeech* (count) — where neither a reliable citation number nor a clean lineage could be established.

**Unverified / null citation counts.** Many records report **"n/a"** citations because the Semantic Scholar API was rate-limited (HTTP 429) during data collection, or because the paper is an arXiv-only / brand-new 2025 preprint. These were left null rather than fabricated. This affects, among others: FreezeD, DM-Font, TIM-GAN, MixNMatch, Multilayer GAN Inversion, FsFont, HeSer, ElasticDiffusion, EraseDraw, Stable Flow, MALT Diffusion, VideoLifter, CamCo, 4K4DGen, and most 2025 entries. Several of these are known to be heavily cited domain baselines (e.g., FreezeD, FsFont, HeSer) despite the missing number.

**Workshop-version vs. canonical-version mismatch.** Several citation counts reflect only the early arXiv stub and *understate* true impact because the weight sits with a renamed/extended publication:
- *Fix the Noise* (2 cites) → CVPR 2023 extension carries the impact.
- *The Nuts and Bolts of Adopting Transformer in GANs* (4 cites) → STransGAN carries the weight.
- *Balancing Reconstruction and Editing Quality* (0) → WACV 2024 version.
- *'Tax-free' 3DMM* (0) → "Removing the Quality Tax" (WACV 2024).
- *Towards Safer AI Content Creation* → IMMA (ECCV 2024).
- *Seamless Human Motion Composition* → FlowMDM (CVPR 2024).
- *MagicAnimate* (127) — the mirror's count is described as conservative; likely higher by 2026.

**Tier is lineage-aware, not citation-aware.** Tier 3 frequently reflects *author/lineage* trajectory rather than the paper's own measured impact. Notable low-citation Tier 3 examples: *Network Fusion with Conditional INNs* (3 cites; Stable Diffusion lineage), *Improved Image Generation via Sparse Modeling* (1 cite; Ganz/Elad), *MorphGAN* (n/a; Ruiz → DreamBooth), *ClickDiffusion* (1 cite; → ConceptAttention), *Spatial Steerability of GANs* (n/a; → VGGT). Readers comparing papers purely by citation count should treat tier as an independent, forward-looking signal.

**Ambiguous / unresolved records.**
- *Directional GAN* appears in both the 2020-adjacent and 2021 cohorts in the source data; it is represented as a 2021 entry here, with the 2020 mention noted.
- Awards in the source are heterogeneous (AI4CC-internal awards vs. downstream venue honors such as CVPR Highlight/Oral, CRV Best Paper, ICML Best Paper for related work). The "Award" fields in Section 2 and the table preserve the source's award labels verbatim; some denote the *follow-up* paper's award rather than the AI4CC entry's.
- A handful of records describe re-presentations of already-published papers (e.g., *EverLight* = ICCV 2023; *EOPose*, *VideoHandles*, *HyperNVD* = CVPR 2025 main conference), so their "AI4CC year" is the presentation year, not the original publication year.

**Scope.** One record is dated 2019 (*Semantic Hierarchy Emerges in Deep Generative Representations*) and is included for completeness as part of the GenForce lineage, though it predates the 2020-2025 window in the title.
