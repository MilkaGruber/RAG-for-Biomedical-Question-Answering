# RAG experiment results

## Run 1

**Run time:** 2026-08-20T21:28:14.396620+02:00

### Configuration

| Parameter | Value |
|---|---|
| embedding_model | sentence-transformers/all-MiniLM-L6-v2 |
| model_name | Qwen/Qwen2.5-1.5B-Instruct |
| num_questions | 500 |
| num_documents | N/A |
| top_k_values | [15] |
| question_only | False |
| document_field | content |
| max_input_tokens | 32768 |
| baseline_cache_file | baseline_predictions.json |
| seed | 42 |
| index_file | textbook_faiss.index |
| results_file | rag_results.json |
| resolved_index_file | textbook_faiss.sentence-transformers_all-MiniLM-L6-v2.content.index |
| resolved_baseline_cache_file | baseline_predictions.Qwen_Qwen2.5-1.5B-Instruct.json |

### Results

| Method | Correct | Accuracy | Difference | Fixed | Broke | Invalid |
|---|---:|---:|---:|---:|---:|---:|
| Baseline Qwen | 205 | 41.00% | N/A | N/A | N/A | 0 |
| RAG (k=15) | 236 | 47.20% | 6.20% | 89 | 58 | 0 |

### Question results

#### 1. Amount of heat that is required to change boiling water into vapor is referred to as

- **ID:** 39c933d9-6014-4f3d-9b81-cb67eb2ec6b9
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Latent Heat of vaporization
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 2. In Ricketts esthetic plane, lower lip rests:

- **ID:** 0d3453ee-77ef-400b-9e64-4ff5b6cbfcc8
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. 2 mm posterior to plane
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 3. Which score is used for wound infection

- **ID:** 4080f3a3-a88c-4bcb-a8a3-2add0483fca0
- **Subject/topic:** Surgery / unknown
- **Gold answer:** B. Southampton score
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 4. All of the following are true about Ifosfamide except:

- **ID:** a45d9322-2e84-4b76-aa18-537bd856d604
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** D. Less neurotoxic than cyclophosphamide
- **Baseline answer:** C (incorrect)
- **RAG k=15:** D (fixed)

#### 5. All of the following are true regarding tonsillectomy in children except:

- **ID:** 5e7cb3e3-57f6-4748-96dd-0b8f6e2fa902
- **Subject/topic:** ENT / unknown
- **Gold answer:** A. Extracapsular approach is best for cold approach
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 6. A 55 years old male patient presents with 4 cm x 5 cm lump in right neck. FNAC assessment revealed it to be a squamous cell carcinoma. Clinical assessment of the oral cavity, pharynx, hypopharynx and larynx did not yield any tumor. Whole body PET scan did not show any increased uptake except for the neck mass. A diagnosis of unknown primary was made. According to AJCC system of classification, the TNM status of the tumor would be:

- **ID:** 0ab83c33-04bd-468e-804e-50dce1bdfa19
- **Subject/topic:** Surgery / unknown
- **Gold answer:** D. TxN2aMx
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 7. The component that sensitizes bacteria and virus to UV irradiation

- **ID:** 9c1caee2-628f-4a80-b55e-8480760cb634
- **Subject/topic:** Microbiology / unknown
- **Gold answer:** D. Nucleic acids
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 8. Which of the following is true about Catlan's appliance?

- **ID:** 2e8bf810-fae5-49c4-8d7d-b27d8073d414
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. It is constructed on the lower anterior teeth with an inclined plane
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 9. In female adrenal gland secretes which hormone?

- **ID:** 6bd02755-f813-46d8-87ff-e40297a2a949
- **Subject/topic:** Physiology / unknown
- **Gold answer:** D. DHEA
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 10. Diminution in normal size of the body, well proportioned body, fine sparse hair on the head and other hairy regions wrinkled atrophic skin and often hypogonadism could be diagnosed as suffering from:

- **ID:** 5d66114f-40b7-4270-92d5-50be1cda6b61
- **Subject/topic:** Medicine / unknown
- **Gold answer:** B. Hypopituitarism
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 11. Intra-epithelial bulla are found in

- **ID:** 3645e915-e8a7-44fe-8cad-734ce6b71063
- **Subject/topic:** Pathology / unknown
- **Gold answer:** A. Pemphigus
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 12. Which of the following is characteristic of T.B. otitis media -

- **ID:** 693c8309-0775-4b3a-899a-5fd7064993f3
- **Subject/topic:** ENT / unknown
- **Gold answer:** D. Multiple perforation
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 13. A 14 year old boy has delayed eruption of the
second molar. Radiography shows a dentigerous cyst surrounding the crown of the tooth. The treatment of choice is:

- **ID:** fcbb415d-5122-4a17-8042-196d3e5add29
- **Subject/topic:** Surgery / unknown
- **Gold answer:** D. Expose the crown and keep it exposed
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 14. Which of the following is not true about latent phase of labour?

- **ID:** 00b083b3-b213-4b45-bbc4-301c4156576c
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** C. Patient may present with false labour due to mild cramps
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 15. Sodium nitroprusside is metabolized to form an active metabolite. This active metabolized to form an active metabolite. This active metabolite of sodium nitroprusside act activation of:

- **ID:** cb022556-5a47-402a-b52c-725b6c314e83
- **Subject/topic:** Pharmacology / AIIMS 2018
- **Gold answer:** C. Guanylate cyclase
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 16. Without supervision, allowed to give dentures

- **ID:** ad724a47-320a-4b79-81d9-8bea8da0f4a5
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Denturist
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 17. Which of the following movements are performed by a non — working condyle?

- **ID:** 7405ebae-1cba-48c4-bf16-8dea393e97ee
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Down wards forwards and medial
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 18. Iron enters enterocyte by :

- **ID:** 72b14998-6b80-45d4-ad70-9766f94e8026
- **Subject/topic:** Biochemistry / AIIMS 2019
- **Gold answer:** A. Divalent cation transpoer
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 19. Halo effect surrounding the root of tooth on IOPA X-Ray is seen with?

- **ID:** 80ca7074-85db-4ead-9b69-23c32b811d94
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Periapical-periostitis
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 20. For which of the following, you will not perform pulpectomy?

- **ID:** 8abcdea2-c351-4df7-ab42-8898201f9949
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Primary teeth with furcation pathology
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 21. Which of the following gingival retraction cord is used in hypertensive patient?

- **ID:** 4682d46d-f791-48cc-ac4d-b2a73fbb18c4
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Retraction cord with 8% aluminium chloride
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 22. A 22 year old college boy with history of sex with commercial workers came to Derma OPD with lesion in genital region, tissue from this lesion was examined, which is the most likely finding?

- **ID:** 7cc17f9f-5ecd-4e71-b32f-74fdf3a6537b
- **Subject/topic:** Microbiology / AIIMS 2019
- **Gold answer:** A. Intracytoplasmic vacuolations
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 23. All of the following are signs of respiratory insufficiency except:

- **ID:** 83190d93-147b-4abc-a5fc-500371388fd5
- **Subject/topic:** Surgery / unknown
- **Gold answer:** D. All of the above
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 24. An 8–day old breast–fed baby presents with vomiting, poor feeding and loose stools. On examination the heart rate is 190/minute, blood pressure 50/30 mmHg, respiratory rate 72 breaths/minute and capillary refill time of 4 seconds. Investigations show hemoglobin level of 15 g/dl. Na 120 mEq/l, K 6.8 mEq/l, Cl 81 meq/l, bicarbonate 15 mEq/l, urea 30 mg/dl and creatinine 0.6 mg/dl. the most likely diagnosis is –

- **ID:** 74af945a-56c6-4b18-935d-388c29f19a56
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** B. Acute tubular necrosis
- **Baseline answer:** B (correct)
- **RAG k=15:** D (corrupted)

#### 25. CLED media better than Macconkey media

- **ID:** dec39d56-fcb3-4cf1-8e83-e09a09a8ce6e
- **Subject/topic:** Microbiology / AIIMS 2019
- **Gold answer:** A. It stimulates growth of Staph and Candida as it is non selective
- **Baseline answer:** A (correct)
- **RAG k=15:** C (corrupted)

#### 26. During relining procedures fear lies in the alteration of

- **ID:** 95835bf6-f013-4b4e-9a46-c3f046eeca17
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Vertical dimension
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 27. Which of the following are most sensitive to X-ray?

- **ID:** a66c89b4-55c2-4708-acfd-07987a4f5347
- **Subject/topic:** Radiology / unknown
- **Gold answer:** A. Tooth buds and salivary glands
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 28. On laboratory investigations in a patient. pH = 7.3, pCO2 = 35 mm Hg. What is the likely acid base imbalance?

- **ID:** 747359d5-2ce7-439e-b229-d04381853421
- **Subject/topic:** Medicine / unknown
- **Gold answer:** B. Metabolic acidosis
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 29. Modification spaces are:

- **ID:** 99d8d535-2f50-4aeb-8e2e-f798f1aca579
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Spaces other than the original class
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 30. Mandibular molars show how many patterns of Accessory Canals

- **ID:** 19afce3e-10f9-4d17-95ad-58e6de9f4ca2
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. 3
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 31. Which of the following change can be done in insulin structure so that there is least change in the function of insulin:

- **ID:** 8ecc6a1a-b653-4b05-81f1-341c356e6c62
- **Subject/topic:** Biochemistry / AIIMS 2019
- **Gold answer:** B. Interchange of B29 and B30
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 32. Preganglionic parasympathetic fibres to the Otic ganglion are carried in the:

- **ID:** f1457bfc-13d3-40bb-9ad9-c6ec7f6c00dd
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** B. Lesser petrosal nerve
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 33. Maximum alveolar aerial oxygen difference is seen in:

- **ID:** f8c972d0-7aa8-45f7-a333-823c27dd5db8
- **Subject/topic:** Physiology / unknown
- **Gold answer:** A. Pulmonary embolism
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (fixed)

#### 34. Most common complication during ridge split or bone spreading is

- **ID:** bdb5ddab-b229-4775-a698-62d03c559af1
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Facial plate splitting
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 35. Which of the following is the most common inherited malignancy :

- **ID:** f4adbaa0-775b-4ef4-89e6-5f8b8290d6d9
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** B. Retinoblastoma
- **Baseline answer:** C (incorrect)
- **RAG k=15:** B (fixed)

#### 36. A pregnant lady acquires chickenpox 3 days prior to delivery. She delivers by normal vaginal route which of the following statement is true?

- **ID:** a05c8cf2-b0bc-496e-b5fd-51467952e2ca
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** D. Baby will develop neoatal varicella syndrome
- **Baseline answer:** D (correct)
- **RAG k=15:** B (corrupted)

#### 37. Which of the following is not an etiological factor for pancreatitis?

- **ID:** ff42704e-3996-4abe-a5b6-574344e7aaf0
- **Subject/topic:** Surgery / unknown
- **Gold answer:** C. Islet cell hyperplasia
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (fixed)

#### 38. All of the following are the complications in the new born of a diabetic mother except –

- **ID:** 8a5481db-d909-4ff3-9f52-52f004f3c6fb
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** B. Hyperglycemia
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 39. AIDS, secondary infection will be all except

- **ID:** 1ca4f1ef-d7dd-4909-bb00-e0c5700e2bf8
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Rubella
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 40. Which of the following is having Maximum buffering capacity

- **ID:** 662c0f6c-a3d9-48a4-b21a-0cc20ef76b87
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** A. Histidine
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 41. Which acid is formed in the citric acid cycle?

- **ID:** acb04c70-4617-4968-9f93-ad46bc9fb8e8
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** A. Oxaloacetic acid
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (fixed)

#### 42. Which primary tooth resemble premolar

- **ID:** dd210467-68c5-4566-9cad-34e5ffa22bc9
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Upper 1st molar
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 43. The lateral lingual swellings and tuberculum impar give rise to:

- **ID:** 4839c894-ec48-45dc-b147-f2e81c11f78a
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** B. Anterior 2/3 of tongue
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 44. In uncontrolled diabetes mellitus, elevated triglyceride and VLDL levels are seen due to:

- **ID:** b8e2e066-a036-4d14-8364-4e91a93812d5
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** B. Increased activity of hormone sensitive lipase and decreased activity of lipoprotein lipase
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 45. A 16 years old girl came for evaluation of primary amenorrhea. She was having hirsutism, irregular bleeding and infeility, diagnosed as PCOS. Which of the following drugs should not be given?

- **ID:** 876a5607-e467-4745-b315-13812c405904
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** B. Tamoxifen
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 46. In anteriors labial surface is formed from

- **ID:** d79a6a3c-0b37-4f9f-aeb9-483298fdb4e2
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. 3 lobes
- **Baseline answer:** C (correct)
- **RAG k=15:** B (corrupted)

#### 47. All of the following are developed from Meckel's cartilage except:

- **ID:** c6f28135-76b7-4762-bd13-839b1592e3d3
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** D. Stapes
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 48. Which of the following is an example of placebo?

- **ID:** 16759fbf-ac94-4ec3-9fde-0702eee3eac5
- **Subject/topic:** Pharmacology / AIIMS 2017
- **Gold answer:** C. Sham surgery
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (fixed)

#### 49. Treatment of postpartum hemorrhage is all except:

- **ID:** 16bc295d-3db6-4565-a611-b677ced1de6b
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** C. Oestrogen
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 50. Interdental papilla protruding from the rubber dam, most common cause is

- **ID:** 04d0e5cc-1355-4028-8d94-47046d188bd2
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Punch are placed too close
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 51. A young marathon runner is paicipating in a marathon competition. After running for 100 m, he develops at the anteromedial aspect of tibia which was mild to sta with, but increased on fuher running. X ray was normal. The doctor ordered a bonescan. What is the likely diagnosis?

- **ID:** baacab5b-7e28-4b0d-b78e-73253e5c7dde
- **Subject/topic:** Orthopaedics / AIIMS 2019
- **Gold answer:** C. Shin splint
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 52. A patient who is a known case of CKD has complaints of vomiting. His ABG repos are as follows: pH - 7.40, pCO2 - 40, HCO3 - 25. Na -145, chloride-100.

- **ID:** 37439d71-3558-4ceb-85af-8332c259afe1
- **Subject/topic:** Medicine / unknown
- **Gold answer:** D. High anion gap metabolic acidosis with metabolic alkalosis
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 53. Drug acting on cell wall of gram positive bacteria:March 2009

- **ID:** 643e9f4a-030c-45b2-867a-2393445afea3
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** D. Vancomycin
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 54. Which of following is an oral precancer?

- **ID:** abd87919-d7f6-44cd-b4c8-8e70630084b5
- **Subject/topic:** Pathology / unknown
- **Gold answer:** D. Speckled Leukoplakia
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 55. Thiamine is a cofactor for all of the following enzymes except:

- **ID:** 8dd9b27b-3aa1-425b-8db6-e935a38d4c5f
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** C. Succinate dehydrogenase
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (fixed)

#### 56. A tooth can be made to appear shorter by positioning?

- **ID:** e4ae05a7-2f9c-470b-bd09-226e43e0c31a
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Gingival Height of contour more incisally
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 57. First paranasal sinus to develop at bih is:

- **ID:** 16ce8442-864b-43f1-b815-f9096e55fa54
- **Subject/topic:** ENT / unknown
- **Gold answer:** A. Maxillary
- **Baseline answer:** A (correct)
- **RAG k=15:** C (corrupted)

#### 58. The oral findings in erythroblastosis fetal's include

- **ID:** b8e55476-5037-418e-afe3-2d7ca5174a31
- **Subject/topic:** Pathology / unknown
- **Gold answer:** C. Pigmented teeth
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 59. How will you check the functioning of an ICD tube?

- **ID:** 6343810a-6571-4662-b3a6-aa7e13a7c65b
- **Subject/topic:** Surgery / AIIMS 2017
- **Gold answer:** B. By observing the movement of air water column in the tube during respiration
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 60. Known Hypertensive patient with BP of 170/120, what will be done for oral prophylaxis

- **ID:** a20495a2-6aba-40db-b41b-fb328e3a8d00
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Sent him back to physician
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 61. Maximum chances of fracture are present when which of these forces are present on a bone:

- **ID:** be3afdad-0f5b-4443-8293-746222d73844
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. Tension
- **Baseline answer:** D (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 62. Pure left sided failure may be seen with –a) ASDb) Aortic stenosisc) Patent ductus arteriosusd) Pulmonary valvular obstruction

- **ID:** 52d643b9-6455-43f0-a04e-a838bf1ba1c8
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** C. bc
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 63. Stainless steel orthodontic wire can be hardened by: (OR) Bending orthodontic wire at room temperature is an example of

- **ID:** b2ea1b5d-abd4-426d-823c-facdd2547357
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Work/ Strain hardening
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 64. Boiled lobster syndrome is seen in poisoning of:

- **ID:** efbacdd9-1c25-4697-8ad9-377c7a8105b8
- **Subject/topic:** Forensic Medicine / unknown
- **Gold answer:** A. Boric acid
- **Baseline answer:** A (correct)
- **RAG k=15:** D (corrupted)

#### 65. Anterior limit of infratemporal fossa is:

- **ID:** 808e56de-bf9d-4a6d-acbe-e27ef3880361
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** B. Maxillary posterior wall
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 66. According to 2011 census, life expectancy at birth for male and female is

- **ID:** 0d73cb93-a494-457a-ae8c-274d92d0947f
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. 67 and 70
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 67. What is the usual weight of rabbit used in ophthalmological experiments?

- **ID:** 360f90ec-189e-464a-a60d-ed9d9bda46ef
- **Subject/topic:** Ophthalmology / unknown
- **Gold answer:** B. 1.5-2.5 kg
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 68. Enlargement of the blind spot occurs in which of the following

- **ID:** 09657fa4-eeb3-4860-8b8c-f2e25c7eabab
- **Subject/topic:** Ophthalmology / AIIMS 2019
- **Gold answer:** D. Papilledema
- **Baseline answer:** C (incorrect)
- **RAG k=15:** D (fixed)

#### 69. Cross-sectional studies are carried on

- **ID:** 51250c61-30fe-47d0-b5cf-e9ce5abcac6e
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Different individuals of different age groups
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 70. In which type of lesion 'eburnation' of the dentine is seen?

- **ID:** 3164ca7d-4050-4da4-87c2-41f1a8d10cb0
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Arrested caries
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 71. Uses of atropine are A/E -

- **ID:** a1a782cf-d0f2-4645-a96d-79ef0cef3516
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** D. Miotic
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 72. Criteria for infant at risk?

- **ID:** 5b612728-c228-4423-8fd8-fde0ff1d3f68
- **Subject/topic:** Gynaecology & Obstetrics / AIIMS 2019
- **Gold answer:** C. Preclampsia is pregnancy
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 73. A 10 year old girl presented with fever convulsions, neck rigidity. CSF findings are protein 150 mg, sugar 40 mg, chloride 2500 mg with lymphadenopathy –

- **ID:** 0778d314-486a-4af0-b2bd-cab83e7e2166
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** D. Tuberculous meningitis
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 74. A 10 year old child came to the OPD with pain and mass in right lumbar region with no fever, with right hip flexed. The pain increased on extension and X ray showed spine changes. Most probable diagnosis is:

- **ID:** 1146bb08-e590-4323-a743-83bc2d531045
- **Subject/topic:** Surgery / AIIMS 2017
- **Gold answer:** A. Psoas abscess
- **Baseline answer:** A (correct)
- **RAG k=15:** C (corrupted)

#### 75. Maximum permissible dose of Articaine in a healthy patient is

- **ID:** 3ca099a7-086a-411e-917e-295561ebb22b
- **Subject/topic:** Surgery / unknown
- **Gold answer:** D. 7 mg/kg
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 76. The primary site of action of antidiuretic hormone is on the:

- **ID:** 9694e5f6-a417-49f7-a455-7a8d08c68f5c
- **Subject/topic:** Physiology / unknown
- **Gold answer:** A. Distal tubules and collecting ducts in the kidney
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 77. Nerve fibres in pulp are

- **ID:** cf208fc9-f8b2-47d0-b02e-df0f6acf4f59
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Sympathetic efferent post ganglionic
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 78. A patient sustained A and endotracheal intubation was done. Most likely GCS score of such a patient would be:March 2013 (b, c, d)

- **ID:** 5c0f862f-2651-4ed4-88d4-2456dab0f036
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. 8
- **Baseline answer:** C (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 79. The aspirate from a keratocyst will have:

- **ID:** 1e482c1e-4aee-48a7-9e4f-c480cc00a094
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. A low soluble protein content
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 80. Frankfort - horizontal is a reference plane constructed by joining which of the following landmarks?

- **ID:** 1879dad4-5bba-48db-bc78-07c64447bf24
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Porion and Orbitale
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 81. Which of the following marked arrow represent lateral semicircular canal during coical mastoidectomy:

- **ID:** afd502ff-b700-4ecf-acec-f849331dd1ed
- **Subject/topic:** ENT / AIIMS 2017
- **Gold answer:** C. C
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 82. Which of the following blade angle is appropriate for scaling and root planing

- **ID:** 5ce754b8-b358-4270-9bd1-8828700a19b1
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. B
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 83. Immunologicaly active cells are:

- **ID:** 59fcd56f-73e9-49e5-8cd0-8097402935ec
- **Subject/topic:** Physiology / unknown
- **Gold answer:** A. Plasma cells
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 84. Polishing of composite is problematic due to

- **ID:** 01c50678-d06f-4894-b7b7-0562a413164e
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Soft matrix and hard filler particles
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 85. Which is a gypsum product?

- **ID:** 39e499a6-b162-4cdf-81e4-c131f7d157c5
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. All of the above
- **Baseline answer:** D (correct)
- **RAG k=15:** B (corrupted)

#### 86. CASE -2 SR visit again but the condition is not improved but this time IV cannula was set. What drug should be given now?

- **ID:** 03952f72-4223-48bc-a0df-51af60400a7a
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** B. I/V Phenobarbital
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (fixed)

#### 87. In excitable cells, repolarization is closely associated with one of the following events:

- **ID:** 860d2715-9c6e-4814-894d-48362fb1235d
- **Subject/topic:** Physiology / unknown
- **Gold answer:** C. K+ efflux
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 88. Mucocutaneous circumoral pigmentation is found in:

- **ID:** 674233e6-009a-41ce-b61d-c9a344dce090
- **Subject/topic:** Pathology / unknown
- **Gold answer:** A. Peutz-Jeghers syndrome
- **Baseline answer:** A (correct)
- **RAG k=15:** C (corrupted)

#### 89. Repeated fracture of a porcelain fused to metal restoration is primarily due to

- **ID:** ef893ac0-92b0-4689-984d-7eade2d8cf53
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Inadequately designed framework
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 90. Which of the following is known as corner stone of behavior management:

- **ID:** 61743cfc-eb0c-46e4-a5ee-a26761c03561
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Tell Show Do.
- **Baseline answer:** B (correct)
- **RAG k=15:** C (corrupted)

#### 91. Property affected due to diameter of nerve fiber/axon?

- **ID:** 75ea3569-eb32-44a0-81dd-705aa50c2769
- **Subject/topic:** Physiology / unknown
- **Gold answer:** A. Conduction velocity
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 92. If during an application of an orthodontic force, the level declines to zero between activations then the force duration is classified as:

- **ID:** 362bf8a9-de7e-48dd-aecf-3ecd13b280b8
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Interrupted force
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 93. Tooth develops from: (Or) Calcified structures of
oral cavity develops from

- **ID:** a1e41d9c-2e03-4195-a5c9-73ee0ac1b8d1
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Ectoderm, mesoderm
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 94. A 4 year old child sustained a fracture in central incisor one month ago. On examination, a necrotic pulp was seen with no other pathological findings. The treatment of choice is:

- **ID:** 62b9add2-a5e9-451f-92c2-2eee629ee143
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Endodontic treatment and root canal filling with ZOE
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 95. Not true about NRHM

- **ID:** d8e3d7c2-cf2f-4dad-a3ad-50352f228de4
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Health and family welfare societies
- **Baseline answer:** D (incorrect)
- **RAG k=15:** C (fixed)

#### 96. Transfusion-associated malaria has a shoer incubation period because of the presence in blood of:

- **ID:** a432db53-67f5-4865-af52-18edf81d1225
- **Subject/topic:** Microbiology / unknown
- **Gold answer:** A. Trophozoites
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 97. All of the following are true regarding Duncan placental separation except:

- **ID:** 3d8328fb-d689-401d-b68f-18a7fe581ee4
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** A. Most common method of placental separation
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 98. One unit of PRBC raises HCT by: (In exam instead of HCT, they wrote HCV, which we assume to be a spelling error):

- **ID:** 0f589144-f2e9-4377-850f-9dc2aaf127da
- **Subject/topic:** Surgery / unknown
- **Gold answer:** C. 3-5%
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 99. The cause of bone destruction in juvenile periodontitis is:

- **ID:** 93645af3-21d4-4a69-bd63-b181635715f4
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Reduced neutrophilic chemotaxis
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (fixed)

#### 100. plate endings are features of

- **ID:** dfdb6250-ea23-4154-b381-ff16ea720fb8
- **Subject/topic:** Physiology / unknown
- **Gold answer:** B. Nuclear bag fibres
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 101. Caries tetralogy by Newburn includes the fourth factor, which is:

- **ID:** e0471ba9-d328-4924-b5e1-6d036b3005b6
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Time.
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 102. The depth of clinical gingival sulcus is the distance between the gingival margin to the

- **ID:** fde19aa5-8a95-46c2-bbf9-5421b8d83b41
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Apical penetration of the probe
- **Baseline answer:** C (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 103. Which disease affects neurons only

- **ID:** e3b61d23-b64b-4b3e-86a8-5b0c08cfd375
- **Subject/topic:** Medicine / unknown
- **Gold answer:** A. Spinocerebellar ataxia
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 104. After cleaning and pumicing the tooth surface, plaque formation takes place within

- **ID:** 11efa366-1d2d-48a8-a247-a362a0447140
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. 1/2 to 1 hour
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 105. In which of the following conditions is the role of microbial plaque most obscure:

- **ID:** 18feef0f-7e8e-4eca-b9b3-57f3973b9a5b
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Desquamative gingivitis
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 106. What does low volume of distribution of a drug mean?

- **ID:** 20cbdec0-d488-4dcf-9630-2707c948390a
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** B. Does not accumulates in tissues
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 107. Normal Curvature seen in Lumbar

- **ID:** b6b91d49-7a30-4a9a-91e6-b2f20341470c
- **Subject/topic:** Orthopaedics / AIIMS 2018
- **Gold answer:** A. Lordosis
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 108. Post-auricular ecchymosis in cases of fracture of the base of the skull is called:

- **ID:** ce3daa75-37fc-41ba-b0ea-80182c3f9e5b
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. Battle's sign
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 109. In which one of the following mixed dentition analysis of deciduous dentition, there is no use of radiographs?

- **ID:** 57336e68-8096-4fa9-89f5-36c05dcd5482
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Moyer's analysis
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 110. Facial nerve is located?

- **ID:** e85ab3af-b295-4750-853a-9fb9389bf2bb
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Below SMAS and below parotidomassetric fascia
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 111. All are sensory to the palate except:

- **ID:** 27a55dd4-2931-4c86-ba40-7f3b341c9b34
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** D. Hypoglossal nerve
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 112. Increased VDO results in

- **ID:** c54d9bde-0f32-4f38-a236-875013438ba9
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. All of the above
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 113. Increased Monocytic count is seen in Typhoid and which of the following conditions?

- **ID:** 5ca66e2e-503b-4847-a729-c8be53fa9325
- **Subject/topic:** Medicine / unknown
- **Gold answer:** B. Sub-Acute Bacterial Endocarditis
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (fixed)

#### 114. Which of the following is not true about screw feed technology

- **ID:** 22c12f88-d394-4d93-8be6-336a477a51b4
- **Subject/topic:** Social & Preventive Medicine / unknown
- **Gold answer:** C. Ideal for pathological waste
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 115. In universal pro-taper retreatment file end cutting tip is seen in?

- **ID:** 9ba1d3cf-434c-4f68-ab5f-0ccbe263e3a5
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. D-1
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 116. Which of the following is true regarding blood transfusion of packed RBC?

- **ID:** 1cd85138-84f2-4c99-aede-bfd10b5ec9b9
- **Subject/topic:** Pathology / AIIMS 2018
- **Gold answer:** B. Should be completed within 4 hours of receiving from blood bank
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (fixed)

#### 117. Drug of choice for scrub typhus is:

- **ID:** fe55c8c7-c6ba-4882-a3c0-15171d62e603
- **Subject/topic:** Pharmacology / AIIMS 2017
- **Gold answer:** C. Doxycycline
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 118. A patient is taking drugs for rheumatoid ahritis and has a history of cataract surgery 1 year back, the patient presented with sudden painless loss of vision, probable diagnosis is?

- **ID:** da529e73-61fe-4b52-81b1-8686b6a62ffd
- **Subject/topic:** Ophthalmology / AIIMS 2018
- **Gold answer:** C. Chloroquine toxicity
- **Baseline answer:** D (incorrect)
- **RAG k=15:** C (fixed)

#### 119. Which is not a feature of wilson\'s disease in a child –

- **ID:** 893ad532-01e8-421e-ac71-d5e8dfb882e5
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** B. Sensory changes
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 120. Indirect Retainer is placed:

- **ID:** 1b9ecfa4-d168-458c-891c-e3a30b5f6e77
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. As far as possible from fulcrum line
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 121. An imaginary occlusal curve that contacts the buccal and lingual cusp tips of mandibular buccal teeth is called the

- **ID:** 2d2d97d9-cb57-4636-897d-6cdb3223544c
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Wilson curve
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 122. Continuous GnRH therapy is used in All EXCEPT.

- **ID:** e7b8728f-9131-4f14-a004-68731f829ef6
- **Subject/topic:** Gynaecology & Obstetrics / AIIMS 2019
- **Gold answer:** C. Male infeility
- **Baseline answer:** B (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 123. Valvular lesion most often resulting from myocardial infarction is:

- **ID:** d454ee11-50e1-475c-b73f-e1c32f66d980
- **Subject/topic:** Medicine / unknown
- **Gold answer:** C. Mitral regurgitation
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 124. Dapsone is used for treatment of bacterial and fungal infections as well as for immunomodulatory actions. What is mechanism of dapsone for these indication?

- **ID:** bb46d4ce-440a-4cea-ab6f-75ce99cdd3aa
- **Subject/topic:** Pharmacology / AIIMS 2018
- **Gold answer:** D. Competition with PABA in folic acid synthesis
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 125. An adolescent male patient came with pain in calf muscles on exercise. On biopsy excessive amount of glycogen present was found to be present in the muscle. What is the most likely enzyme deficiency?

- **ID:** 7f8086d8-e91b-40fc-8d8c-55cc74f84d6c
- **Subject/topic:** Biochemistry / AIIMS 2018
- **Gold answer:** D. Phosphorylase enzyme
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 126. Reticular fibers of collagen tissues are present in all of the following except:

- **ID:** 46c8e8cf-5930-486f-ad11-99b9339c12ab
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** A. Thymus
- **Baseline answer:** C (incorrect)
- **RAG k=15:** A (fixed)

#### 127. A 3 days old baby is admitted with intraventricular hemorrhage. Baby develops abdominal distention. The X-ray abdomen showed pneumatosis poalis. Stage the necrotizing enterocolitis:

- **ID:** 83b776f2-ae9a-42ec-8262-931b29af2d9f
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** C. 2b
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 128. Enzymes are classified according to:

- **ID:** 8a42a6cc-3a47-4af9-ad8f-4aeacca7f382
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** A. Action on substrate
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 129. 99.73 variation involves how many SD?

- **ID:** 700240f4-b59e-4dcb-a1c1-0d082a4b9643
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. 3
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 130. Marked reduction in amount of dentin, widening of predentin layer, presence of large area of interglobular dentin and irregular pattern of dentin is seen in

- **ID:** 71a5084e-36a1-4cc3-bee0-9de613f5fd24
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. Odonto dysplasia
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 131. Hypoxic Ischemic encephalopathy true is –

- **ID:** e16742f8-aa56-4a27-9d8d-b7643e5f27c5
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** C. Seizure
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (fixed)

#### 132. Amount of energy actually producing cutting is:

- **ID:** a7f65c0f-ed0f-47f3-96d1-f4f85ff5c3a0
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Cutting efficiency.
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 133. Lidocaine is used more commonly in dentistry because lidocaine :

- **ID:** 30cf8c11-4a20-47e4-bb0e-1113d5ae34a2
- **Subject/topic:** Surgery / unknown
- **Gold answer:** C. Causes lesser incidence of allergic reactions
- **Baseline answer:** B (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 134. Which of the following scoring system is used for wound infection?

- **ID:** 8e0eacd3-9755-426d-b1c5-2bff71295f88
- **Subject/topic:** Surgery / AIIMS 2019
- **Gold answer:** C. Southampton score
- **Baseline answer:** C (correct)
- **RAG k=15:** B (corrupted)

#### 135. Dentin island are frequently found in the root canals of which of the following permanent teeth

- **ID:** ce4bf55c-99a1-41a9-9107-cdab91e7e11b
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Upper 2nd Premolar
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 136. Electric resistance between oral mucosa and PDL is always constant that is:

- **ID:** e0c3fa32-b170-46e4-a748-9965e38ca3a9
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. 6.5 K ohm
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 137. Maximum amount of phosphate is seen in

- **ID:** 5951aa74-d30c-4c33-b1e6-dd5e5d103ca0
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Enamel
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 138. Perception of taste even in absence of stimuli is known as

- **ID:** ee31cc18-91fd-4582-a3e8-5311e85521b3
- **Subject/topic:** Pathology / unknown
- **Gold answer:** D. Phantoguesia
- **Baseline answer:** D (correct)
- **RAG k=15:** A (corrupted)

#### 139. Which of the following nucleus has cardio inhibitory function?

- **ID:** f6445d02-67c1-458d-8983-debf90b50ebc
- **Subject/topic:** Physiology / unknown
- **Gold answer:** A. Nucleus Ambiguus
- **Baseline answer:** C (incorrect)
- **RAG k=15:** A (fixed)

#### 140. Suitable	technique	used	for	diagnosis	of	posterior
interproximal caries in children

- **ID:** 51973390-3173-4aa1-b318-974ac57a6f7b
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Bite wing with RVG
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 141. Asseion: In a patient admitted to hospital for community acquired pneumonia, combination therapy of beta lactams and azithromycin is given.Reason : This combination covers gram positive organisms and anaerobes.

- **ID:** a9b0fecd-41ee-4e52-87a9-12e7048e6615
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** B. Asseion is true but reason is false.
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 142. The maxillary sinus drains into the

- **ID:** ab0bf88b-ad5b-482b-b45a-61ac9a5b3d58
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. Middle meatus
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (fixed)

#### 143. Acetone free methyl alcohol is present in Leishmann's stain for:

- **ID:** df493519-1b08-442e-853c-edd9ca4f6f57
- **Subject/topic:** Pathology / unknown
- **Gold answer:** D. It stops metabolic and enzymatic activity of the cell
- **Baseline answer:** D (correct)
- **RAG k=15:** A (corrupted)

#### 144. Which of the following finding are there in iron deficiency anemia?

- **ID:** 0447b9a2-22ec-449c-8a23-a52c28ac6b34
- **Subject/topic:** Pathology / AIIMS 2019
- **Gold answer:** A. | TIBC, | Ferritin, | Transferrin saturation
- **Baseline answer:** A (correct)
- **RAG k=15:** D (corrupted)

#### 145. Lactobacillus count AFTER CARIES ACTIVITY test is 10,500CFU. What is the rate of caries progression ?

- **ID:** e70b5eab-a54e-49a7-a8ca-0d226e856a54
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Severe
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (fixed)

#### 146. What causes malignant hyperpyrexia?

- **ID:** a40481b2-dbe1-4b5b-aa7f-20b3d47d8779
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** D. Suxamethonium
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (fixed)

#### 147. 10-year-old boy visits dentist with complicated crown fracture with abscess formation in 12. X-ray reveals radiolucency in relation to 11, 12. 12 is having immature  blunderbuss canal while 11 has complete root formation, vitality of 11, 21 is negative. What would be the management of this patient?

- **ID:** 17cb7e3f-0ca7-4937-a407-76bf9f401143
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Revascularization in 12 and RCT of 11
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 148. A G3P2, pregnant comes to your clinic at 18 weeks of gestation for genetic counselling. She has a history of two kids born with thalassemia major. Which test would you recommend now?

- **ID:** 014ba2fe-d596-4265-bf46-616641ea4a9f
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** C. Cordocentesis
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 149. Chances of ankyloses of mandibular molar which is autotransplanted depends on?

- **ID:** edb0ef61-a009-4fe9-811e-5b9d6ea40435
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Surgical extraction of molar
- **Baseline answer:** C (incorrect)
- **RAG k=15:** B (fixed)

#### 150. All of the following affects bur efficiency except:

- **ID:** 112694f0-3fab-4d28-84a7-ebf4721eee1b
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Head length and diameter
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 151. A patient was given ampicillin 2 g intravenously. After that, the person developed rash on skin, hypotension and difficulty in breathing. The patient should be managed by

- **ID:** 24662938-a2a7-4328-846d-1887c22ff54c
- **Subject/topic:** Pharmacology / AIIMS 2019
- **Gold answer:** A. 0.5 ml of 1:1000 adrenaline by intramuscular route
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 152. Which of the following Universal pro-taper re-treatment file has end cutting tip?

- **ID:** bfd5b74e-0d0c-4c69-9a3c-b700bd269d40
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. D1
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 153. Gold Standard for evaluation of any obstruction in the nasal pathway:

- **ID:** 2e4dea82-5bec-438e-a674-0f317e467e70
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Rhinomanometry.
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (fixed)

#### 154. Poor prognostic indicator of ALL is –

- **ID:** acc7b73e-20f6-40c7-b831-d8b45a8f38fb
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** D. Hypodiploidy
- **Baseline answer:** D (correct)
- **RAG k=15:** B (corrupted)

#### 155. All of the following statements about cast cobalt
alloys are true EXCEPT:

- **ID:** aa2241ec-9245-4448-81c8-523222ef466f
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. They have higher ductility than gold alloys.
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 156. intermediate of kreb cycle used in heme synthesis;

- **ID:** 422e1a54-04f3-4193-ac55-61c4ae8b23a9
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** A. succinyl-CoA
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 157. Arestin is:

- **ID:** 3cf954d4-ea8b-4c75-b70d-2e86af595b9c
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. 2% minocycline
- **Baseline answer:** C (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 158. About polymerization shrinkage of composite all are true, except:

- **ID:** 015438df-2f7d-4298-9da3-f15b1fcef278
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Polymerization shrinkage is greater if bonded surface area is lesser than unbounded surface area
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 159. Which of the following injection is available for subcutaneous administration?

- **ID:** 59110b4f-4074-4293-aa6d-96b1a6b49b82
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** B. Terbutaline
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 160. Gene for Dentin mineralization

- **ID:** 8bbcb007-44f0-460f-9e73-25f6006859fe
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. PHEX
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 161. Interstitial fluid volume can be determined by:

- **ID:** 074d6dbc-2825-4387-ada2-01725dd954e2
- **Subject/topic:** Physiology / unknown
- **Gold answer:** D. Radioactive sodium and radioactive labelled albumin
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 162. Which is associated with defect in DNA repair

- **ID:** 8b84483e-3b11-4c8b-8e10-ba9f512b7341
- **Subject/topic:** Pathology / unknown
- **Gold answer:** A. Xeroderma pigmentosum
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 163. Lente insulin is composed of:

- **ID:** 441684f3-9823-4e41-9066-c572118e3efc
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** A. 30% Amorphous + 70% Crystalline insulin
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 164. Lymph from lower lip-middle part drains directly into:

- **ID:** 46d8350b-3f1d-4199-9c82-aaff47498fdd
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** B. Submental nodes
- **Baseline answer:** C (incorrect)
- **RAG k=15:** B (fixed)

#### 165. Soft tissue curettage is used for:

- **ID:** a0c6e73e-5ed5-42b5-a71c-24e031f7e7e8
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Shallow pockets with gingivitis
- **Baseline answer:** B (incorrect)
- **RAG k=15:** A (fixed)

#### 166. A 49 years old male with 35 pack years presented with painless mass in left scrotal sac and microscopic hematuria. On laboratory investigation, Alphafetoprotein and lactate dehydrogenase was negative. What is the most probable diagnosis?

- **ID:** dc918205-fb3a-42a9-805e-ec2c3e1c7352
- **Subject/topic:** Surgery / unknown
- **Gold answer:** C. Renal cell carcinoma
- **Baseline answer:** B (incorrect)
- **RAG k=15:** C (fixed)

#### 167. Which of the following is caused by Amphotericin B

- **ID:** 8cced5f0-0647-4f31-9ba7-71bebcfb2255
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** A. Hypo kalemia
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 168. Which is the most common site for fracture in zygomatic arch fracture?

- **ID:** 71e11d65-2238-4a3f-9b41-bfb7218c66e5
- **Subject/topic:** Surgery / unknown
- **Gold answer:** C. Posterior to zygomaticotemporal suture
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 169. find false statement regarding sensory endings

- **ID:** 31913a50-8459-47c0-b142-7a31df3f16c3
- **Subject/topic:** Physiology / unknown
- **Gold answer:** A. Annulospiral wrap the ends
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 170. Acetyl choline release can be increased from presynaptic membrane by:

- **ID:** fec4f95e-7c1c-4e3e-9245-18cc14fe84e9
- **Subject/topic:** Physiology / AIIMS 2019
- **Gold answer:** C. Blocking voltage gated K+ channels on presynaptic membrane
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 171. Young’s formula for calculating pediatric dose of a drug is:

- **ID:** c4021919-6161-4c71-9f5d-f34b079667f7
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Age / Age+12 x Adult dose
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 172. You have been called to declare a brain dead l2-year-ord chitd in pICU, all ofthe given are signs of brain death except?

- **ID:** 47987536-7408-420b-9f9a-9e968f645ae6
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** D. Decoicate and decerebrate posturing
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 173. Feed forward mechanism..

- **ID:** 4eb2c660-2893-450f-957c-536b6a6f9b3d
- **Subject/topic:** Physiology / AIIMS 2019
- **Gold answer:** C. Salivation on smelling food
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 174. A child's behaviour is traced to have dental difficulties
from	his	mother.	The	most	satisfactory	method	of
handling the situation is to:

- **ID:** 7b81cd07-3765-4f50-8b28-a88576f4223e
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Modify his fear by familiarization
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 175. Main mechanism of action of heparin Is to prevent:

- **ID:** 3a0e01d0-4230-4633-a7a9-624a0c32a486
- **Subject/topic:** Surgery / unknown
- **Gold answer:** B. Conversion of prothrombin to thrombin
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 176. "Hair-on-end" appearance in a skull roentgenogram is
seen in :

- **ID:** 89e75fc5-d650-40aa-81db-cee3759ce219
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. Thalassemia
- **Baseline answer:** C (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 177. Patient with severe acidosis is treated with

- **ID:** 70f851da-1d36-4d09-a9f0-f7afc63c07ff
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. i.v. NaHCo3
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 178. Open reduction of condylar fracture is strongly indicated in
(Or)
Absolute indication for open reduction in condylar fractures

- **ID:** 1c392503-537c-4926-a3bc-3daf8ddefeb3
- **Subject/topic:** Surgery / unknown
- **Gold answer:** B. Lateral displacement of the condyle (or) Lateral fracture dislocation condyle
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 179. Pulpectomy and pulp capping are more successful in
primary teeth because of:

- **ID:** fe1e7fd7-eab7-4ce9-a865-8c02fb21022b
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Increased blood supply through the wide apex
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 180. The enamel has no capacity of self —repair because

- **ID:** 515dde1e-02e3-41d5-a88f-3d2a99421bde
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Its formative cells are lost once it is completely formed
- **Baseline answer:** C (incorrect)
- **RAG k=15:** B (fixed)

#### 181. In penicillin allergy, penicillin acts as a:

- **ID:** ca49d5c3-9678-4b4f-b10d-4021802c636d
- **Subject/topic:** Microbiology / unknown
- **Gold answer:** A. Hapten
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 182. Key indicator for AFP surveillance ?.

- **ID:** 7c6fe266-845b-4f4b-8ddb-ca5d016e0396
- **Subject/topic:** Social & Preventive Medicine / unknown
- **Gold answer:** D. At least one case of non-polio AFP per year per 100000 population of under 15 years
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 183. Which growth factor Is not present in PRP?

- **ID:** a4d559cf-a0bb-4eab-9cd6-023fceb916ad
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. PDGF cc
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 184. Thickness of luting cement is:

- **ID:** 88082d18-5e7b-4c2a-81fa-b91139c7276d
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. 20-40 μ
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 185. Which of the following is the complication of massive blood transfusion?

- **ID:** e5be7962-590f-4590-bb2b-84860a14a42a
- **Subject/topic:** Pathology / AIIMS 2019
- **Gold answer:** B. Metabolic alkalosis
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 186. A 48 years old female presents with seizure, recurrent gross hematuria and left flank abdominal pain. Abdominal CT reveals left perinephric hematoma with 3 cm angiomyolipoma along with multiple right renal angiomyolipoma measuring 1.5 to 6.5 cm. What would be the most probable diagnosis?

- **ID:** 20f29076-98f9-479b-a77b-96fae28d5689
- **Subject/topic:** Surgery / unknown
- **Gold answer:** C. Tuberous sclerosis
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 187. All are signs of impending Eisenmenger except –

- **ID:** 84fe7359-1ad3-4031-bf62-e4474bb33a86
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** A. Increased flow murmur across tricuspid & pulmonary valve
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (fixed)

#### 188. An elderly male patient presented with fever, chest pain, and dry coughp; sputum culture showed growth on Charcoal Yeast Extract Medium, the organism is

- **ID:** 8e686bff-ca17-4507-89bc-cce7d6ab9e7f
- **Subject/topic:** Microbiology / unknown
- **Gold answer:** C. Legionella
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 189. In post splenectomy patient, chances of Infection with which of these Increases:

- **ID:** 9ac4d9c7-db9d-4521-83bc-f6f58f6d5db7
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. Encapsulated bacteria
- **Baseline answer:** B (incorrect)
- **RAG k=15:** A (fixed)

#### 190. Determining level of fluoride in community water fluoridation programme depends on:

- **ID:** 4d8af4ad-1f62-4bb8-a485-439992b3af49
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Mean annual temperature of the place
- **Baseline answer:** D (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 191. Centrineuraxial (spinaland epidural) anaesthesia is not contraindicated in

- **ID:** 8ecb4d6b-8ab1-40d7-af48-fa8fe50bd21f
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** B. Patient on aspirin
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (fixed)

#### 192. In biopsy true about formalin as fixative is all except

- **ID:** 6ba7a8b3-b653-4208-8815-75c03f1088b4
- **Subject/topic:** Pathology / unknown
- **Gold answer:** D. 2% forrnaline is used
- **Baseline answer:** C (incorrect)
- **RAG k=15:** D (fixed)

#### 193. Which of the following is not a function of guiding plane?

- **ID:** d958d68a-5fb2-4e85-bbb3-fda0acb43676
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Engage the abutment tooth in such a manner as to resist displacement of restoration away from basal seat
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 194. Enzymes help by:

- **ID:** ff410d96-12d4-43ba-8b24-7bfbd8ad360c
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** A. Lowering the activation energy
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 195. All are secondary colonizers except

- **ID:** 53d58d7a-d546-4b1a-88a7-fa7348ff08a5
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. S. sanguis
- **Baseline answer:** C (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 196. Dental plaque adheres to the tooth because:

- **ID:** 2dd66c3e-9b8c-421e-818b-5770ed270bfe
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Dextrans are insoluble and sticky
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 197. A young male patient is on 5 mg haloperidol for many days, recently for last 4 days of duration he has inner restlessness and urges to move. Diagnosis is?

- **ID:** bdc34663-b39a-47bb-b034-7f804e437c09
- **Subject/topic:** Psychiatry / AIIMS 2017
- **Gold answer:** A. Akathisia
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 198. Ameloblastoma histologically resembles:

- **ID:** 17aac19b-ed5d-4038-9f3a-ec0c7478012e
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. BCC
- **Baseline answer:** A (correct)
- **RAG k=15:** C (corrupted)

#### 199. Stable element in Ti6Al4V in alpha phase is?

- **ID:** e342fc89-9875-4188-9009-b9065fdf5b9c
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Al
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 200. First local anaesthesia to be used clinically was

- **ID:** 53208a86-eac2-46ae-8ae3-703e1afda738
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. Cocaine
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 201. Diagnosis of the following ECG-

- **ID:** 18d5c4a1-cb81-41a8-9bfc-b6f7dec431d2
- **Subject/topic:** Medicine / AIIMS 2017
- **Gold answer:** B. Electrical alternans
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 202. Which of the following is not used for making indirect wax pattern?

- **ID:** 0919bffa-ea11-4e1f-9139-4c20fcd1a394
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Utility wax
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 203. True about ythT cells:

- **ID:** 96d449da-7560-45e2-aa9b-2b5a74296f25
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. Oligoclonal proliferation
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 204. Pickling is done:

- **ID:** bdc7d080-b3a4-4edb-acc4-08a35d181e75
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. To remove oxide film from casting
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (fixed)

#### 205. T-lymphocytes play a primary role in

- **ID:** 4e3061f9-0a14-4878-9abd-6a0459b268b8
- **Subject/topic:** Physiology / unknown
- **Gold answer:** B. Production	of	lymphokines	and	delayed hypersensitivity
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 206. Which of the following drug must be sold only on production of a prescription by a registered medical practitioner?

- **ID:** 65bef933-00cc-4f7b-8ca0-a77f2fe92c57
- **Subject/topic:** Pharmacology / AIIMS 2018
- **Gold answer:** A. Schedule H
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 207. Infective endocarditis is most commonly seen in:

- **ID:** 97bd8c32-3ea6-41e1-856e-b9a91d20e643
- **Subject/topic:** Medicine / unknown
- **Gold answer:** B. VSD
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 208. In a female, intraocular metastasis most commonly occurs from which of the following gynaecological primary?

- **ID:** 770a2934-5df3-4d53-a79c-0d4358b95016
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** A. Breast
- **Baseline answer:** B (incorrect)
- **RAG k=15:** A (fixed)

#### 209. Submandibular duct is exposed via intraoral approach by incising the:

- **ID:** f3dc5246-3f28-4033-aec4-be283724f4ed
- **Subject/topic:** Surgery / unknown
- **Gold answer:** B. Mucous membrane
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 210. Postherpetic neuralgia is defined as pain lasting beyond how many weeks?

- **ID:** 725d9973-1082-4c9b-b4fb-9c63a4615e63
- **Subject/topic:** Skin / unknown
- **Gold answer:** D. 4 weeks
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 211. The type of bone present in the inter-radicular area is

- **ID:** 41c672e1-f83d-487a-a284-399e766a33a9
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Cancellous
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 212. A lady complains of headache, nausea and tenderness in temporal region with migraine. On microscopic investigation what will be seen

- **ID:** 5963ab9b-34a2-4d45-acc6-d7688d671080
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. Giant cell arteritis
- **Baseline answer:** B (correct)
- **RAG k=15:** C (corrupted)

#### 213. Phallic stage of Freud corresponds to which of the following stages of Piaget

- **ID:** d18484d7-55a9-4be3-9ba6-59cdd44d1bdf
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Pre operational
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 214. A 26 years old healthy female got pregnant for 1st time and LSCS was done for fetal distress. Mild hypeension was present during pregnancy. Two days after delivery she had headache and seizures but proteinuria was not seen. CT scan shows 2 x 3 cm parasagittal hematoma. Diagnosis is:

- **ID:** 0fc0b4ce-9bfd-48a2-920d-88c67e2c4e9c
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** C. Sagittal sinus thrombosis
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 215. The cyst which is found within the bone at the junction of the globular process, the Lateral nasal process & maxillary process is:

- **ID:** 2ffd16e8-5b32-40c9-9aa6-1cab59d5728e
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. Globulomaxillary cyst
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 216. Which of the following statements is true about Swyer svndrome?

- **ID:** 16f0079a-a1c9-4a10-a9c7-2fa11f8bddba
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** A. Can be feile with surrogacy
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 217. Migratory motor complexes in the gut reappear after intervals of:

- **ID:** be168ef1-fee0-4f80-9c60-6259e78b56b9
- **Subject/topic:** Physiology / unknown
- **Gold answer:** B. 90 minutes
- **Baseline answer:** C (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 218. A man comes with history of abnormal excessive blinking and grunting. He says he has no control over his symptoms, which have risen in frequency of late. This has staed affecting his social life making him depressed. Which of the following medications should be used in him?

- **ID:** 8729556c-a513-42d6-abc1-ed7f6c9ca397
- **Subject/topic:** Psychiatry / unknown
- **Gold answer:** A. Risperidone
- **Baseline answer:** B (incorrect)
- **RAG k=15:** A (fixed)

#### 219. Microscopic examination of chromosomes shape, size and arrangement is known as

- **ID:** c57fffae-d994-4330-aece-6019507ac1c0
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. Karyotyping
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 220. Which of the following is true about prostate cancer?

- **ID:** 228da52b-1c04-49cc-bfd8-05701a0fdb11
- **Subject/topic:** Surgery / AIIMS 2019
- **Gold answer:** A. Histopathology is determined by Gleason score
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 221. Natural disaster causing maximum deaths

- **ID:** 1348a664-1ccc-422f-a083-91d77cb24b92
- **Subject/topic:** Social & Preventive Medicine / unknown
- **Gold answer:** A. Hydrological
- **Baseline answer:** B (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 222. A patient of hypeension on Metoprolol, Verapamil was given. This is will result in?

- **ID:** 0489f20c-a0ce-4251-9eec-e8d5e691a49e
- **Subject/topic:** Medicine / AIIMS 2018
- **Gold answer:** B. Bradycardia with AV Block
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 223. The anemia associated with leukemia

- **ID:** b674d02e-af50-4f16-9f81-e3983a854b6a
- **Subject/topic:** Medicine / unknown
- **Gold answer:** C. Myelophthisic type
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 224. The ETDRS cha is used for visual evaluation in diabetic patients. What does ETDRS stand for

- **ID:** bee78f93-a09e-491f-856e-846b81e4aa5c
- **Subject/topic:** Ophthalmology / unknown
- **Gold answer:** B. Early treatment for diabetic retinopathy study
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 225. Preferred haemostatic agents for perforation repair include all except?

- **ID:** 89dc8003-fb16-432a-9da3-4d8464ca9ab8
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Ferric Sulphate
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 226. The diameter of the tip of a periodontal probe is:

- **ID:** 5115d601-c567-4a71-a53a-e4a7facd703b
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. 0.5 mm
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (fixed)

#### 227. A 38 years old female presented to the emergency with extensive burns. The patient had grade 3 burns on the face, back, upper arms and forearms along with singeing of hairs. Which of the following is not a proof of inhalation burns?

- **ID:** 4c0b406e-5d78-4f1d-99ca-c51f8d240e4f
- **Subject/topic:** Forensic Medicine / unknown
- **Gold answer:** A. Yellow colored sputum
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 228. A young female presents to OPD with a spontaneous aboion and secondary amenorrhea since then. FSH was found to be 6 IU/mL. What is the most probable cause of amenorrhea?

- **ID:** 3745bf96-43aa-40b2-ae62-3be01c0f92a4
- **Subject/topic:** Gynaecology & Obstetrics / AIIMS 2018
- **Gold answer:** D. Uterine synechiae
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 229. Moality associated with emergency abdominal aoic surgery is:

- **ID:** 28709e53-cbb8-48d9-aa3e-44aaa7037257
- **Subject/topic:** Surgery / unknown
- **Gold answer:** C. 40%
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 230. . The prospectively evaluated, double-blinded, randomized clinical trail represents the 'gold-standard' for providing evidence for therapeutic decision making. This was first proposed by the father of evidence-based medicine:

- **ID:** 7912bdab-3d26-40a1-91c3-9d52e760b930
- **Subject/topic:** Social & Preventive Medicine / unknown
- **Gold answer:** B. Sackett
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 231. A patient presented with pain in the right lower quadrant of abdomen. He has history of renal stones in right kidney. He was prescribed an opioid which is agonist at kappa receptors and antagonist at mu receptors. The likely drug given was:

- **ID:** 2f6be3a1-0736-4ec3-9e42-aa9732e401d6
- **Subject/topic:** Pharmacology / AIIMS 2017
- **Gold answer:** A. Pentazocine
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 232. A young male present with loose motions and intermittent abdominal pain over the past 1 year. Wet mount stool specimen showed the presence of multiple ova which are more than 100u in diameter. The causative organisms for the disease shall not include?

- **ID:** e4749151-5d65-4cf3-b663-67e75d1da084
- **Subject/topic:** Microbiology / unknown
- **Gold answer:** D. Opisthorchis viverrini
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 233. In chronic renal failure : a) Urine output is more than 3 litres per dayb) Urine concentration is decreasedc) Sodium conservation is poord) Polycythemia is present

- **ID:** f2f90872-25be-4295-9e2c-26f8310a2100
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** C. bc
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 234. A 35 years old male comes with complain of baldness. On examination, well-defined bald patches were seen with no scarring. Small broken hairs were seen in the surrounding area. What is the likely diagnosis?

- **ID:** 344d849d-fe32-41d8-853f-b02b41028d71
- **Subject/topic:** Skin / unknown
- **Gold answer:** B. Alopecia areata
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 235. Which of the following require delayed separation?

- **ID:** 30f6c7b2-824b-431b-a84e-f8bdb0554946
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. All of the above
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 236. Which material undergoes hysteresis?

- **ID:** 1bcc4893-9641-4f95-95c7-8c81492eb9a9
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Reversible hydrocolloid
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 237. True about bisphosphonate mechanism of action

- **ID:** 46669fd0-e19c-4e9c-bdc4-836d0d9771f4
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Inhibit osteoclast mediated resorption
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (fixed)

#### 238. Wilson curve seen in:

- **ID:** 8977896a-04f0-4605-bd65-94da2269da22
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Molars
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 239. Only tooth in which buccal surface is made of 2 lobes

- **ID:** bd1f87b7-50d6-4060-a9a3-f281c15a1898
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Upper 1st molar
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 240. ICD-10 stands for

- **ID:** 15811471-d00e-471c-adf9-2edc497bb4ce
- **Subject/topic:** Social & Preventive Medicine / unknown
- **Gold answer:** C. International Classification of Diseases, 10th revision
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 241. For >10 mm setback of mandible, which of these surgeries is most suitable:

- **ID:** f7d9f997-d9d6-40e0-a921-49bb343f8b52
- **Subject/topic:** Surgery / unknown
- **Gold answer:** B. Vertical ramus osteotomy
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 242. Which of the following cry is characterized by loud, high pitched and siren-like wail:

- **ID:** 6dfdea6c-4c96-49dc-8b65-a57b59d87036
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Obstinate cry.
- **Baseline answer:** A (correct)
- **RAG k=15:** C (corrupted)

#### 243. Drug not given in PCOD in a 30-year-old lady with infeility?

- **ID:** c5bc52bf-c316-48d2-9c03-ed4ac17338ab
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** B. Tamoxifen
- **Baseline answer:** C (incorrect)
- **RAG k=15:** B (fixed)

#### 244. Vasopressor of choice in pregnancy is:

- **ID:** c34c9996-5391-4655-9249-948fe2cb0d2b
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** A. Ephedrine
- **Baseline answer:** C (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 245. Endocrine glands that are not influenced by the pituitary gland include the:

- **ID:** 6920ce2b-f9c9-49aa-9e6e-c94aeb13e709
- **Subject/topic:** Physiology / unknown
- **Gold answer:** B. Adrenal medulla, parathyroids, and the islets of langerhans
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 246. All of the following are true for light cure composite except:

- **ID:** 22f5d1c3-8073-452a-937e-63414dc5065e
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Polymerization reaction continues for a period of 72 hours
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 247. Which of the following is a tool used in gene editing?

- **ID:** 543b341f-7350-4a9b-9bc6-63a1a2cee1e8
- **Subject/topic:** Pathology / unknown
- **Gold answer:** A. CRISPR
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 248. Which of the following groups of fibres are not attached to alveolar bone?

- **ID:** e0952660-983f-4990-a8c6-d6b6bc19aca3
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Transseptal
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (fixed)

#### 249. Organic component of bone comprises of:

- **ID:** d60d9642-e4b5-4c01-b004-4422e0fb084e
- **Subject/topic:** Surgery / unknown
- **Gold answer:** D. 90% collagen protein
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 250. Basically TMJ is a:

- **ID:** 721f44cb-907c-46d5-af80-9606cc9e5023
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Diarthrodal joint
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 251. What to be done next?

- **ID:** 7879facb-4a0b-424e-9997-25aae47a52aa
- **Subject/topic:** Orthopaedics / AIIMS 2019
- **Gold answer:** B. Bone biopsy
- **Baseline answer:** C (incorrect)
- **RAG k=15:** B (fixed)

#### 252. Syncope is usually caused by:

- **ID:** 635aedc6-993c-483d-a192-04e327b6a438
- **Subject/topic:** Surgery / unknown
- **Gold answer:** B. Cerebral ischemia
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 253. Enzymes, which play an important role in calcification, are:

- **ID:** 1c4db599-706a-4089-9b53-5ec331a651af
- **Subject/topic:** Physiology / unknown
- **Gold answer:** C. Alkaline phosphatase and pyrophosphatase
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 254. After a building collapse, among remnants, a person's length of humerus is 24.5 cm. What is the predicted height of this person?

- **ID:** 8db7e145-052a-4774-9a5f-db3c4e9ac1d6
- **Subject/topic:** Forensic Medicine / unknown
- **Gold answer:** C. 130 cm
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 255. Morris retractor is most commonly used to retract

- **ID:** f010ab15-2d53-4002-a0d8-308dc27650c5
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. Left hypochondrium
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 256. All of the following muscles have parallel oriented fibers except:

- **ID:** 5986807f-c9d7-43ca-951a-2c4be8c0d62e
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** D. Tibialis anterior
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (fixed)

#### 257. The red blood cells in beta thalassemia are typically:

- **ID:** d052235a-dcdc-46e0-89e5-992eed6dc580
- **Subject/topic:** Medicine / unknown
- **Gold answer:** B. Microcytic and hypochromic
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 258. Which of the following is clinical use of tafenoquine?

- **ID:** 28e47981-c859-48ad-a4b9-14a13c5b3a34
- **Subject/topic:** Pharmacology / AIIMS 2019
- **Gold answer:** A. Radical cure of Plasmodium vivax
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 259. Enamel hatchet is differentiated from chisel by all except:

- **ID:** 67a5354d-9a42-436a-be77-eacc7d10cd7c
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Blade is perpendicular to the long axis of handle
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 260. Facial nerve innervates all of the following except:

- **ID:** e9be346c-4d68-4290-9ca4-5ea76f8d2280
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** B. Anterior belly of digastric
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 261. Midazolam cannot be given by which of the following routes:

- **ID:** 3f41f911-cf5c-4227-b32b-7efd0b2fc191
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Inhalation
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 262. Which is not true about vibrio cholera

- **ID:** f23569ea-da84-4e74-aa14-69c64f04424d
- **Subject/topic:** Microbiology / unknown
- **Gold answer:** D. Cannot survive in extracellular environment
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 263. A 6 year old patient with extra cusp on maxillary central incisor is associated with all, except

- **ID:** d4549997-d19b-48eb-bd9a-aa3c29c82dec
- **Subject/topic:** Pathology / unknown
- **Gold answer:** D. Proteus Syndrome
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 264. Which is the best index for burden of disease?

- **ID:** 46653ca7-d61a-4d6a-a135-91309eff9b49
- **Subject/topic:** Social & Preventive Medicine / unknown
- **Gold answer:** D. Disability adjusted life years
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 265. true statement about golgi tendon organ is

- **ID:** e81f9080-63a6-4b59-88a1-28ed69c13055
- **Subject/topic:** Physiology / unknown
- **Gold answer:** D. 3-25 muscle fibres
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 266. Ritonavir inhibits metabolism of all of the following drugs except:

- **ID:** d1d3d999-2032-48cf-87c7-5bcd25acb18b
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** B. Phenytoin
- **Baseline answer:** D (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 267. Most advantageous indication of acid etching is

- **ID:** 0cfefe19-7cba-424e-928a-b462add52180
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Decrease micro leakage
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 268. In leukemia patient, post extraction bleeding doesn't stop because of:

- **ID:** e3782486-d6bf-4ef2-8830-5cdfdcacb020
- **Subject/topic:** Radiology / unknown
- **Gold answer:** C. Platelet disorder
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 269. The organ most resistant to GA is

- **ID:** ea10b02c-4402-4a16-9bec-03cc31e8587d
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** B. Medulla oblonagata
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 270. Intensifying screen is used in extraoral radiograph to:

- **ID:** 1730e3d6-7a73-4485-bc27-65e8ad61c9bb
- **Subject/topic:** Radiology / unknown
- **Gold answer:** A. Decrease radiation to patient
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 271. A patient reported with Disto-oclusal amalgam restoration in 47 & complaints of sticking of food in interproximal area. Most common reason is?

- **ID:** 418ea8f5-7225-4daa-9fa7-2cf9724b9a8b
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Contact area too gingivally
- **Baseline answer:** D (correct)
- **RAG k=15:** C (corrupted)

#### 272. True about LDL receptor:

- **ID:** f87f02ae-e248-473d-9a03-5a866b0dfbee
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** D. All of the above
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 273. A 23 years old boy, a badminton player, sustained injury of left ankle. He was immobilized for 3 months, the cast was removed and patient was able to walk normally. Later he complained of pain and swelling in the left calf, left ankle and foot. His mother massaged him for 30 minutes. After a while he developed acute onset of breathlessness and was brought to emergency and died. Most likely cause of death is:

- **ID:** a4c17223-91e0-454d-95af-18ddf9a97e41
- **Subject/topic:** Medicine / unknown
- **Gold answer:** A. Pulmonary thromboembolism
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 274. Which of the following is ture about afferent nerve fibers of pulp

- **ID:** 165c772a-9b32-48fe-b94e-fe949ec9cb9a
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Sympathetic post ganglionic
- **Baseline answer:** D (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 275. Which of the following does not or permissive euchromatin due to changes occurring at cytosine residues at CpG islands in DNA?

- **ID:** 678018c2-3154-4411-937e-0e5d4116739f
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** A. Methylation
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 276. For supporting complex amalgam restoration, which of the following cement has best modulus of elasticity?

- **ID:** 93308f4a-1927-4596-981a-58f373a9707e
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Zinc phosphate
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 277. A person with histrionic, shy, anxious avoidant per!sonality comes under which cluster?

- **ID:** b22457e3-c620-4a3d-bde1-0aa6e6c185a7
- **Subject/topic:** Psychiatry / unknown
- **Gold answer:** C. C
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 278. Most prominent lingual fossa in Incisors is seen in

- **ID:** 7845514d-6bb2-460f-a203-351dffc13abf
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Upper Lateral incisor
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 279. Exact number of weeks between last menstrual period and expected date of delivery :March 2005

- **ID:** cb6588a7-e4ef-4670-b6aa-7eae297fb443
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** C. 40 weeks
- **Baseline answer:** C (correct)
- **RAG k=15:** B (corrupted)

#### 280. IOTN is not used for which malocclusion?

- **ID:** 713b94cf-fc1e-4c32-b28e-f187cf86562d
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Bimaxillary protrusion
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 281. A psychiatrist is not posted at:

- **ID:** 4f50899d-3016-461b-bd81-c1c29fbe6d29
- **Subject/topic:** Social & Preventive Medicine / unknown
- **Gold answer:** A. PHC
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 282. The primitives palate is formed from:

- **ID:** 8cfb49e4-4f0b-4e40-b9f7-2eba10852a63
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** A. Frontonasal process.
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 283. The KRI paste is composed of:

- **ID:** 8d6cd2e6-9912-4bb5-b276-289f11e6371f
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Iodoform, camphor, parachlorophenol and menthol
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (fixed)

#### 284. Child is Evasive and dawdling, what could be the child's mother behavior:

- **ID:** 304d9306-4f11-4078-8b98-7c8f78ff7da3
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Authoritarian mother.
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 285. Enzyme regulating the conversion of ethanol to acetaldehyde:

- **ID:** 876ee705-7f99-4e03-bbf1-77059c2971c0
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** A. Alcohol dehydrogenase
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 286. In SCHWARTZ formula for calculation of creatinine clearance in a child, the constant depends on the following except –

- **ID:** 2a9cc59f-8f5f-4035-8010-07d1cc7a2f64
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** D. Severity of renal failure
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 287. A Jawan posted in Siachen was brought to the emergency depament with hypothermia. Which is the ideal site to measure his temperature?

- **ID:** 22e9f959-2d98-46de-b35c-601974f8d014
- **Subject/topic:** Surgery / unknown
- **Gold answer:** B. Rectal
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 288. Supporting cusps occlude in:

- **ID:** 167c89ae-1898-497f-87c4-805a65c7a9bd
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Both AB
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 289. Which of the following structure is not removed in radical neck dissection-

- **ID:** 2c37d934-7b5e-4e0d-9b34-55ae75466301
- **Subject/topic:** Surgery / unknown
- **Gold answer:** C. Tail of parotid
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (fixed)

#### 290. Human Developmental Index is a composite measure, which uses?

- **ID:** bbb8ca0b-54ed-4f08-a87d-8eef087e37f1
- **Subject/topic:** Social & Preventive Medicine / unknown
- **Gold answer:** D. Life expectancy at bih, knowledge and decent standard of living.
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 291. All are true about CRISPR cas 9 Except

- **ID:** f7da4d3a-cd77-4744-a67a-720973e1eb12
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** D. All of these
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 292. Which of the following are characteristic feature of high copper amalgam alloy?

- **ID:** 60000767-457b-4528-8918-b4da0bc900e4
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Less marginal #
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 293. Patient with increased PT, APTT & TT and normal fibrinogen and platelet counts, diagnosis is?

- **ID:** 3bb33f16-ca92-481f-bb39-b5278156c63d
- **Subject/topic:** Pathology / unknown
- **Gold answer:** D. Vitamin K deficiency
- **Baseline answer:** C (incorrect)
- **RAG k=15:** D (fixed)

#### 294. Largest permanent tooth in mouth is

- **ID:** ba3c920c-6281-42ca-8f2e-45a3dfdc5c3e
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Maxillary 1st molar
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 295. A 10 years old child has intrusion of permanent maxillary central incisor. The choice of treatment is

- **ID:** 77f42ec8-d712-43b7-8160-dd99cad04643
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Allow tooth to erupt on its own (spontaneous eruption)
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 296. Gene commonly indicated in congenital cataract:

- **ID:** 71803632-1b88-4332-88f5-be3ac2515b85
- **Subject/topic:** Ophthalmology / unknown
- **Gold answer:** B. CRYGS-3
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 297. A 22 year old female in emergency presents with sore throat from 3 days, headache and vomiting, blood pressure 90/50, tiny red spots distal to sphygomomanometer cuff

- **ID:** 7d6455c7-5b76-4e75-84e6-0e37f920fa5a
- **Subject/topic:** Medicine / unknown
- **Gold answer:** B. Neisseria Meningitidis
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (fixed)

#### 298. Koebner phenomenon is seen in

- **ID:** c1730172-912a-4744-ad47-3034848202c7
- **Subject/topic:** Pathology / unknown
- **Gold answer:** D. Psoriasis
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 299. Cobalt-Chromium alloys contains:

- **ID:** f186d21a-67e0-4532-bb17-a3b4ac7ccbd2
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. 60% cobalt and 30% chromium
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 300. Antischkow cells are present in all of the following conditions except

- **ID:** 1dc55cbe-41dc-4dda-9e52-cbc66d59d9b6
- **Subject/topic:** Pathology / unknown
- **Gold answer:** D. herpes simplex
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 301. Primary cartilaginous joint is called as:

- **ID:** 10bd1123-5a30-4895-b50c-4d176aa3a858
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** B. Synchondrosis.
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 302. Cephalosporin	active	against	pseudomonas
aeruginosa

- **ID:** 1b7a2a1c-6321-4541-b649-7db8418c38da
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** A. Cefoperazone
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 303. Culture media of candida is:

- **ID:** bd2d1f59-a803-4311-b0b5-65dff935f85c
- **Subject/topic:** Microbiology / unknown
- **Gold answer:** B. Saboraud's medium
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 304. Epidural venous plexus is located in

- **ID:** 1d9fbbc4-e25e-4dc3-bbd5-d0eefd02bd2b
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** D. In vertebral canal above duramater
- **Baseline answer:** D (correct)
- **RAG k=15:** C (corrupted)

#### 305. All are features of benign intracranial hypeension except:

- **ID:** 091c018c-210f-4a46-9b8b-6f2c53d72283
- **Subject/topic:** Medicine / unknown
- **Gold answer:** A. Proptosis
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 306. If multiple firing is done to opaque layer of dental porcelain than It become

- **ID:** bb51425d-0636-48c5-89ca-4358036b933b
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Too glazed
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 307. Resistance to corrosion in a cobalt-chrome casting is due to presence of:

- **ID:** a78209a5-9800-45d5-9cab-4838388d53e7
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Chrome
- **Baseline answer:** C (incorrect)
- **RAG k=15:** B (fixed)

#### 308. Lenolin is added in ZOE paste to:

- **ID:** a9dccfec-0882-4012-aa1b-e74bb18bf47e
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Increase flow
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 309. Toxic shock syndrome is due to the following virulence factor:

- **ID:** a31714d8-1531-4865-8d0d-f2430b8d68c1
- **Subject/topic:** Microbiology / unknown
- **Gold answer:** B. Pyrogenic exotoxin
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 310. Which of the following is not used as a disinfectant?

- **ID:** ced0e6e7-048a-467e-aa7e-e10def9ebb5e
- **Subject/topic:** Microbiology / unknown
- **Gold answer:** B. 100% Alcohol
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 311. The organism which is involved in anaerobic infections of head and neck region is

- **ID:** 97ef7cca-90c3-4c3c-bc58-28d2d5e1bc0b
- **Subject/topic:** Medicine / unknown
- **Gold answer:** D. Bacteroids
- **Baseline answer:** C (incorrect)
- **RAG k=15:** D (fixed)

#### 312. In the odontoblastic layer the following connections is/are found

- **ID:** e6b676f8-26ba-42f6-9bd2-739abf1c039a
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. All of the above
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 313. A 5-year-old child from a rural area presented to the OPD with pustular lesions on the lower legs. The cuture from the lesion showed hemolytic colonies on the blood agar which were Gram-positive cocci. Which of the following reactions would help to provisionally confirm the diagnosis of group A streptococcal pyoderma?

- **ID:** 4cbe210a-0779-4ba7-b599-e9b89fa5a0b1
- **Subject/topic:** Microbiology / unknown
- **Gold answer:** B. Bacitracin sensitivity
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 314. Which of the following are true regarding levator ani EXCEPT?

- **ID:** 8e5ce21c-74ea-4b0d-b929-c03ee9d54765
- **Subject/topic:** Anatomy / AIIMS 2019
- **Gold answer:** A. Levator ani muscle is attached at pelvic brim
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (fixed)

#### 315. A pier abutment is:

- **ID:** e9f104f9-2231-4a49-b5a6-983ca6e08c49
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. With an edentulous space on mesial and distal sides of the abutment
- **Baseline answer:** C (incorrect)
- **RAG k=15:** B (fixed)

#### 316. Normally Maxillary first molar has

- **ID:** e05a465a-5c90-4c80-afda-56d0e6070792
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. 3 roots and 3 canals
- **Baseline answer:** A (correct)
- **RAG k=15:** C (corrupted)

#### 317. In a cerebrohepatorenal syndrome, which of the following accumulate in brain?

- **ID:** af87accb-34b2-42de-be48-16e94bbf22ab
- **Subject/topic:** Biochemistry / AIIMS 2018
- **Gold answer:** C. Very long-chain fatty acid
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 318. 46.	A 9 year old child has increased Horizontal anterior bone loss, less cementum and on test shows excretion of phosphoethanolamine in the urine. The child is suffering from.

- **ID:** e0ec575f-4a30-4a42-a1c8-a0faed766b8b
- **Subject/topic:** Pathology / unknown
- **Gold answer:** A. Hypophosphatasia
- **Baseline answer:** C (incorrect)
- **RAG k=15:** A (fixed)

#### 319. Which of the following is not true about stamp cusp?

- **ID:** 18796d06-7762-4185-b0ca-c1b527502073
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Sharp cusps and prominent ridges are present
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 320. Which of the following drug is commonly used in treatment for cancer associated thromboembotismt

- **ID:** 860f5673-7e87-4a35-ba17-628c738929fa
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** A. Low molecular weight heparin
- **Baseline answer:** A (correct)
- **RAG k=15:** C (corrupted)

#### 321. Treatment of choice for a patient with gonococcal as well as non-gonococcal urethritis is:

- **ID:** fb8c4e20-6d34-461e-8e14-45fcd8c662e4
- **Subject/topic:** Pharmacology / AIIMS 2017
- **Gold answer:** D. Azithromycin 2 g oral single dose
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 322. True about bicuspidization:

- **ID:** 1470a21a-b226-4cd1-904d-85cd841d5afa
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Separation of mandibular molar mesial and distal roots with their respective crown portions
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 323. Pregnant women with following is called systemic hypeension:

- **ID:** ebc190bb-4cbd-4640-9429-8fbd448866dc
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** A. Hypeension diagnosed at 10 weeks of gestation
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 324. In a population of 10000 people, the prevalence of a disease is 20%. The sensitivity of a screening test is 95% and specificity is 80%. The positive predictive value of the test will be -

- **ID:** f8a5b0e2-b529-4ad4-b55d-f6e5fc4708e1
- **Subject/topic:** Social & Preventive Medicine / unknown
- **Gold answer:** B. 54.30%
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 325. Cold agglutinin is

- **ID:** 590217c3-2f56-4547-a6e3-e3d3409bc6e2
- **Subject/topic:** Medicine / unknown
- **Gold answer:** B. IgM
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 326. Fetal adrenals release which hormone predominantly:March 2009, September 2010

- **ID:** 8be32dbe-9a46-4a8a-8c08-ff89c3e78c3d
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** D. Coisone
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 327. Foramen magnum transmits all except:

- **ID:** 590248a6-74f4-45bf-a54a-d9b9b09b78b8
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** D. Both option 2 and 3
- **Baseline answer:** B (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 328. Which acid does not show coagulation necrosis on contact?

- **ID:** 2ab8b27b-1646-4886-8378-f2f11f84a79e
- **Subject/topic:** Forensic Medicine / unknown
- **Gold answer:** C. HF
- **Baseline answer:** D (incorrect)
- **RAG k=15:** C (fixed)

#### 329. Which of the following drugs does not affect DNA synthesis?

- **ID:** b3aa72de-f85c-407f-892b-9dae7d953417
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** B. Linezolid
- **Baseline answer:** C (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 330. To prevent sensitivity caused by acid etching and to protect pulp in deep cavities which of the following should be used.

- **ID:** d2b006ba-21fa-4ec8-bcda-760d55e8b326
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Ca(OH)2 liner
- **Baseline answer:** A (correct)
- **RAG k=15:** D (corrupted)

#### 331. After planning an implant in lower molar region, patient complains of inability to chew by other teeth on same side. What should be your first step in treating this patient

- **ID:** 60a30040-3784-41dc-b81d-be50cde12679
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Check the occlusion in centric
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 332. Replacing amino acid will not change its functions

- **ID:** 7e567a6e-46f6-4f48-bd14-21e53726f1ff
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** A. Glutamine to Asparagine
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 333. Gingival massage increases blood supply in:

- **ID:** 4329bad6-ab20-42bc-8cb5-b89601d7bdee
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Lamina propria
- **Baseline answer:** C (correct)
- **RAG k=15:** D (corrupted)

#### 334. Which of the following show chemical bond with enamel (calcified tissues)?

- **ID:** db180b6d-8b4e-487e-a47d-7c554c8dad2e
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Polycarboxylate cements
- **Baseline answer:** D (incorrect)
- **RAG k=15:** C (fixed)

#### 335. Functions of apoproteins are/is

- **ID:** c36f9d0a-bcf4-44c2-93ef-0f83d3387664
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** D. All of the above
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 336. The number of sites examined to assess the stages of bone maturation in Fishman's skeletal maturation index are:

- **ID:** a0ad23e1-1238-4d3b-b939-33e852d48919
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. 6
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 337. Custom tray is better than stock tray for impression of crown due to following reasons except:

- **ID:** fa8d86dc-9efc-454c-8b47-beccf53b41e3
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Custom tray is cheaper
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 338. Which of the following drug is commonly used for community acquired pneumonia in OPD?

- **ID:** 44f185f0-7a8e-406c-a33a-b2d7d54e7a25
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** C. Azithromycin
- **Baseline answer:** C (correct)
- **RAG k=15:** B (corrupted)

#### 339. False about innervation of parotid gland:

- **ID:** f955fff3-f4ec-41be-a119-a43e2024120e
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** C. Preganglionic parasympathetic nerve begin in inferior petrosal nucleus
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 340. A child can walk upstairs one step at a time, can ride cycle but can't jump can also speak sentences, can tell his/her name gender but finds difficult to narrate the story.What is her actual developmental age

- **ID:** dd6f308c-9900-47f6-b41b-978022bb7700
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** B. 2
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 341. Which cement is irritating to the pulp?

- **ID:** 769fac02-71ac-4554-bade-5d6a9a5edfb4
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Zinc phosphate
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 342. Which of the following does not occur in High Copper Amalgam?

- **ID:** dc8d9432-3981-45b5-b559-6cfaccb013f4
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Penetrating Corrosion
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 343. A 48-years-old male reported to you with fractured central incisor with fracture line extending 4 mm gingival below CEJ with thin bone buccally and thick apicopalatally, treatment of choice is:

- **ID:** 6e7a5d33-133c-414b-9ea5-d7eaa60ff853
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. Socket shield technique
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 344. The best way to remove a hydrocolloid impression from the patient's mouth is:

- **ID:** 30b2fee8-1ce3-4f84-ad72-f20e7b53a24b
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Sudden jerking of the impression to prevent tearing
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 345. Phenol red thread test is used for dry eye:

- **ID:** eaa33fd8-64a3-47a0-b13c-2b49a1f0e37f
- **Subject/topic:** Ophthalmology / unknown
- **Gold answer:** A. In the test, volume of tears is measured as it changes color on contact with tears
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 346. Which periodontal fibres are consistent and are reconstructed even after the destruction of the alveolar bone?

- **ID:** 3ef21987-3285-429c-a8be-5f67efefaaf8
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Transseptal
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 347. A person was advised by his ohopedic surgeon to get regular dressing of his wound done. But the patient did not give much care. During follow-up, patient was repeatedly told to get the dressing done timely but patient didn't do the dressing himself, saying that he was busy. Finally the wound enlarged and the underlying bone developed osteomyelitis. Which of the following statement is true regarding above-mentioned situation?

- **ID:** cd0edc92-8fb3-4f97-b0ce-d74446009179
- **Subject/topic:** Forensic Medicine / unknown
- **Gold answer:** A. Doctor is guilty under "Last clear chance" doctrine
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 348. Acrocephaly is also known as:

- **ID:** 21428c77-d386-4507-bb71-20c05b5f32b6
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** D. All of the above.
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 349. During pregnancy baby can be affected in utero in all except:

- **ID:** a28aea2d-6784-4a02-bd4c-90cb24e64c77
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** D. Polio
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 350. Accessory canals are most numerous in apical third, which one is 2nd numerous in this regard

- **ID:** 2b368176-2ef0-4871-8ae4-b1daae990f34
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Coronal Third
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 351. ‘Fleur -de- lys’ term is used for:

- **ID:** 4d39dabb-c57f-4a2d-a979-fd4347773e76
- **Subject/topic:** Pathology / unknown
- **Gold answer:** A. Dens invaginatus
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 352. Difference in transudate & exudate is that the former
has a:

- **ID:** d4979c9e-6419-4f42-b71d-bec7c5077426
- **Subject/topic:** Pathology / unknown
- **Gold answer:** A. Low protein
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 353. Blood brain barrier is absent in all of the following areas except

- **ID:** 2e81781f-8c3e-4d9a-86b3-a2651e07dce9
- **Subject/topic:** Physiology / unknown
- **Gold answer:** B. Habenuclear trigone
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 354. Embalming without issuing death ceificate is punishable under section:

- **ID:** 5c578aa4-a6fd-4de5-b0f6-adb926564122
- **Subject/topic:** Forensic Medicine / unknown
- **Gold answer:** A. IPC 201
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 355. All are true of paracetamol poisoning expect?

- **ID:** 593f6b1c-c039-46aa-b81e-f418ed39ed6c
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** B. Asymptomatic for 24 to 30 hours
- **Baseline answer:** C (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 356. Oral infection by penicillinase producing organisms should be treated with:

- **ID:** f04e3d13-d50f-45d8-9fc2-82ef57da3aa9
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** B. Dicloxacillin
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 357. Saliva which is formed in salivary glands, when passes from salivary gland to duct orifices, it undergoes numerous ion exchanges and as a result
saliva become ____________ as compared to plasma:

- **ID:** f4f1be65-d615-4550-b159-a85d27b8b518
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Hypotonic
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 358. A patient presents to the ER after a A with multiple rib injuries. He is conscious, speaking single words. RR = 40/min, BP= 90/40 mmHg. What is the next immediate step in management?

- **ID:** 1b4a2a96-cd33-4ccd-bf13-3c208a07983a
- **Subject/topic:** Medicine / unknown
- **Gold answer:** D. Needle inseion in 2nd ICS
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 359. Which of the following is not associated with haemorrhage?

- **ID:** 783aaf31-fd64-4f4e-aa67-93c00cb407ad
- **Subject/topic:** Pathology / unknown
- **Gold answer:** C. Melanosis
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 360. Large anterior fontanelles, open sutures, slanting eyes,
decreased sexual development, macroglossia and enamel hypoplasia are seen in:

- **ID:** 0b98d76f-ea90-4e4e-9af0-881362b7bae3
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. Down's syndrome
- **Baseline answer:** B (correct)
- **RAG k=15:** C (corrupted)

#### 361. Inflammation of the periapical tissue is sustained by:

- **ID:** b02a2fb8-3cd5-4043-88fa-ab4ad3092efe
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Microorganisms
- **Baseline answer:** C (correct)
- **RAG k=15:** B (corrupted)

#### 362. Which of the following is the best study design to assess in quick time the strength of association between smoking and lung cancer?

- **ID:** 2cc7bf03-5a41-4a8c-a8c9-9f969afac49f
- **Subject/topic:** Social & Preventive Medicine / unknown
- **Gold answer:** B. Case controlstudy
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 363. Which of the following doesn't have any effect on pancreatic secretion?

- **ID:** 650ee1f1-18e4-4e45-beaa-94f44eca7de5
- **Subject/topic:** Medicine / unknown
- **Gold answer:** D. Gastric inhibitory polypeptide
- **Baseline answer:** B (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 364. Earliest diagnosis of pregnancy can be established safely by:

- **ID:** 114fa1dd-9f36-4b84-9f6a-68303bc63931
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** A. USG for fetal cardiac activity
- **Baseline answer:** C (incorrect)
- **RAG k=15:** A (fixed)

#### 365. Best graft for alveolar cleft surgery
(Or)
Patient with cleft palate graft taken from

- **ID:** 5a236a74-118f-49b5-adde-21dba36a8bee
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. Posterior iliac crest
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 366. One day after complete mouth extraction, blue black spots are seen on the neck of the patients. These spots indicate:

- **ID:** 87a02021-923f-4cd0-b93d-bfb486c0aa29
- **Subject/topic:** Surgery / unknown
- **Gold answer:** B. Postoperative ecchymosis
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 367. Which of the following increases callus formation:

- **ID:** f1f7b5b5-1446-4c3b-b863-6f933689cb95
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** B. Movement at fracture site
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 368. Post op pulmonary complications are seen/expected in all except:-

- **ID:** 8466f417-6a8e-4f07-87f8-556fb5fac62a
- **Subject/topic:** Anaesthesia / AIIMS 2019
- **Gold answer:** A. BMI>30
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 369. Renal osteodystrophy differs from nutritional and genetic form of osteomaLacia in having:

- **ID:** 0a96136a-d645-4ad6-9f31-53192793e1d0
- **Subject/topic:** Medicine / unknown
- **Gold answer:** D. Hyperphosphatemia
- **Baseline answer:** C (incorrect)
- **RAG k=15:** D (fixed)

#### 370. Which of the following statements about tRNA molecules is false?

- **ID:** 2c0bfd6d-2451-4961-8155-6c0a739e7f1c
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** D. There is at least one tRNA for each of the 2 amino acids
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 371. Gingivitis

- **ID:** 455ebd1d-982f-4a99-948c-8b541e36db40
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Is a reversible lesion
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 372. Calcium ions triggers muscle contraction by binding to:

- **ID:** 21af7233-ae6a-423c-ae71-9148212a37c3
- **Subject/topic:** Physiology / unknown
- **Gold answer:** C. Troponin
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (fixed)

#### 373. What is the location of Meissner's corpuscles?

- **ID:** 8cc0f461-86ab-4fdf-97f4-194da3dc5e26
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** D. Papillary dermis
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 374. A patient shows one or more of the following: advanced bone loss, grade II and III furcation involvements, tooth mobility, inaccessible areas, systemic/environmental factors represents:

- **ID:** c48cca4e-55ef-4a73-b07d-6ac3a3c5c1eb
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Questionable prognosis
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 375. The usual radiographic appearance of an osteosarcoma is:

- **ID:** e536d0d8-52e5-4881-b33e-23907a9a3034
- **Subject/topic:** Radiology / unknown
- **Gold answer:** C. Sunburst pattern with radiopaque strands extending from the cortical plates
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (fixed)

#### 376. Which of the following is not glucogenic?

- **ID:** d0de8433-05e9-4391-ad03-5b228436ccd5
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** C. Acetyl-CoA
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 377. Following bilateral mandibular fracture in the canine region, the following muscles will tend to pull the mandible back:

- **ID:** 07f7dc0f-6050-4d44-b532-71e4d2787bac
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. Genioglossus and anterior belly of digastric
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (fixed)

#### 378. Most common cyst associated with adjoining vital teeth?

- **ID:** 6380bf46-988e-4ed8-8add-f57fa7bb61fc
- **Subject/topic:** Pathology / unknown
- **Gold answer:** A. Dentigerous cyst
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 379. Which type of prefabricated post preparation system in mandibular molar is preferred?

- **ID:** 0a3c5105-0818-4067-88e1-fb89e5d36957
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Parallel, partially cemented
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 380. Before an arbitrary face bow transfer record, the dentist must determine:

- **ID:** 46e4c25f-f518-43a9-bad7-481cb1a16416
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Axial centre of rotation of condyle
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 381. Both ketogenic and glucogenic amino acids as

- **ID:** 5948bf46-bda9-45d2-8165-c12f8387e345
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** A. Isoleucine
- **Baseline answer:** A (correct)
- **RAG k=15:** D (corrupted)

#### 382. Liver is divided into eight segments according to Couinaud's classification based upon

- **ID:** 744e4dce-b8f1-447f-a964-bea1bbe98edf
- **Subject/topic:** Anatomy / AIIMS 2019
- **Gold answer:** B. Poal vein
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 383. Tumor cells in chronic lymphocytic leukemia or small lymphoblastic lymphoma (CLL/SLL) arisefrom which of the following?

- **ID:** 40013980-4b7a-4cc7-8c38-f2f45215bcbf
- **Subject/topic:** Pathology / AIIMS 2017
- **Gold answer:** B. Naive B cell
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 384. Which of the following would you consider ohostatic hypotension?

- **ID:** ee5093ed-0f38-4c1f-a70a-13548b8779f7
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. SBP fall by 20 mm hg, DBP fall by 10 mm hg within 3 minutes
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 385. Complete obliteration of pulp is seen in all except:

- **ID:** e8e87fbd-58db-4141-a400-a8043e303add
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. Type II dentinogenesis imperfecta
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 386. Touidine blue is to:

- **ID:** a59b9fe8-ab81-4f9c-9b65-10df248b3f49
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Differentiate between malignant transformation
- **Baseline answer:** B (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 387. All of the following influence the efficiency of bur, except:

- **ID:** 89e1c450-ada8-47e4-a966-ffe1ad0f789d
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Height of taper of bur
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 388. Infection of masticatory space is usually associated with

- **ID:** 95a455ca-7bba-4432-844f-1d1516a852cc
- **Subject/topic:** Surgery / unknown
- **Gold answer:** B. Mandibular molar
- **Baseline answer:** D (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 389. Which film is used for caries detection? (or) Which film
is used for caries detection in children?

- **ID:** f6bd6944-8c47-4037-8871-10855371a4c2
- **Subject/topic:** Radiology / unknown
- **Gold answer:** D. F speed
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 390. During laparoscopic inguinal hernia repair a tacker was accidently placed below and lateral to the ilio-pubic tract. Postoperatively the patient complained of pain and soreness in the thigh. This is due to the involvement of:

- **ID:** 0fe00e95-fdf2-420f-bc42-8325787a7aae
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. Lateral cutaneous nerve of thigh
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 391. In Rh lso Immunisation, exchange transfusion is indicated if –

- **ID:** 593bd593-3060-493d-bb10-ff9e10e36f17
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** D. All of these
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 392. Ganglionic transmission is mediated by:

- **ID:** 100d2a31-8f28-4500-99c9-67690fe15625
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** D. Postsynaptic nicotinic receptors
- **Baseline answer:** C (incorrect)
- **RAG k=15:** D (fixed)

#### 393. Which of the following prevents fracture of MO amalgam:

- **ID:** 90d508fa-01fd-4b1f-811e-6fc4a0df7054
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Beveling of axiopulpal line angle
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 394. Apoptosis is suggestive of:

- **ID:** 5917b59d-d9f8-4234-b0be-13f9c7325e9f
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. Coagulative necrosis
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 395. What is the dose of adrenaline in anaphylactic shock?

- **ID:** 4127528f-2cc3-44bc-b07e-446577f5018c
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** A. 0.5 ml in 1:1000
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 396. Method of choice for a New born child not passing urine for 36 hours :

- **ID:** 33a697bc-627a-4a24-b381-19c181fcdded
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** A. Ultrasound of kidney & bladder
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 397. Anaerobic glycolysis of which of these produces 3 ATPs per unit glucose consumed?

- **ID:** 587ef917-abf4-4b32-985c-e2020bd397cb
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** D. Glycogen
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 398. Resistance form of endodontics is:

- **ID:** 76e1d3a2-90b6-4735-be99-004263456619
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Resists movement of gutta-percha in apical area
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 399. All of the following are true about augmentation of labor except:

- **ID:** a13b245e-56b4-43cd-84fe-1c83ac2badeb
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** A. Twin pregnancy precludes the use of oxytocin
- **Baseline answer:** A (correct)
- **RAG k=15:** B (corrupted)

#### 400. In which of the following heart diseases maternal mortality is found to be highest ?

- **ID:** 23ce8f17-8358-419a-b2d9-92079d21241b
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** A. Eisenmenger's complex
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 401. A woman comes with postdated pregnancy at 42 weeks. The initial evaluation would be:

- **ID:** 476fc39f-b59d-4878-839c-006da1da3f70
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** B. Review of previous menstrual history
- **Baseline answer:** B (correct)
- **RAG k=15:** D (corrupted)

#### 402. All of the following are true about iron deficiency anemia except:

- **ID:** 27c9ead8-7baf-4c63-bf48-a03e57812c44
- **Subject/topic:** Medicine / unknown
- **Gold answer:** C. Mostly presents without any symptoms with abnormal laboratory findings
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 403. After the delivery of an infant of diabetic mother, blood glucose of the infant was 60 mg/dt. Which other investigation docs the sister expects that the physician would ask her to do?

- **ID:** d3610034-9a33-48ef-ac6e-5fb36e22f076
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** C. Serum calcium
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 404. According to WHO definition, what is the criteria for considering a high endemic area for meningococcal meningitis?

- **ID:** 2dbbf01a-5a68-40c9-a24f-fd4af9d314e8
- **Subject/topic:** Social & Preventive Medicine / unknown
- **Gold answer:** C. >10 per 1,00,000 population
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 405. Lymph from tongue not drained by following vessels

- **ID:** 2617e9f9-7ba9-4f7c-b182-f7dbff771148
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** B. Ventral
- **Baseline answer:** C (incorrect)
- **RAG k=15:** B (fixed)

#### 406. On laboratory investigations in a patient, LDL was highly elevated but the level of LDL receptors was normal. Which of the following is most probable cause?

- **ID:** cf3f103b-e4d8-4f34-86aa-b69f3b31fe55
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** C. Apo B-100 mutation
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 407. Best guide for the management of Resuscitation is:

- **ID:** a963bf66-e44e-445f-b3ba-26efcd836ad9
- **Subject/topic:** Surgery / AIIMS 2017
- **Gold answer:** B. Urine output
- **Baseline answer:** D (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 408. CYP50 inhibition is least by:

- **ID:** 6bce210a-7174-4c76-b1f0-9bc3f5c835fc
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** B. Rabeprazole
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 409. Which of the following is a tertiary monoblock system of obturation of the root canal.

- **ID:** 8e282abb-59be-434b-be33-a0928db221ff
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Active Gutta percha
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 410. Which of the following type of collagen is present in healing and granulation tissue?

- **ID:** f1b944e7-35c7-4ae3-aea7-3cd1d32e5249
- **Subject/topic:** Biochemistry / AIIMS 2018
- **Gold answer:** C. Type III
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 411. Lady wth MS + MR with full term gestation, obstetrician planning to conduct normal delivery, what would be anesthesia of choice?

- **ID:** 6cf0218d-ff22-4f7c-9d54-3f5193fe8b8c
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** D. Neuraxial analgesia
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 412. Cells most commonly affected in glaucomatous optic atrophy?

- **ID:** 3aff7082-0082-4114-a47b-d68bf127c263
- **Subject/topic:** Ophthalmology / unknown
- **Gold answer:** C. Ganglion cells
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 413. During exercise in physiological limits what is the effect on end systolic volume?

- **ID:** 97a54f46-0d5e-4979-820c-ab311c30f08a
- **Subject/topic:** Physiology / AIIMS 2018
- **Gold answer:** A. ESV decreases
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 414. Use of lithium during pregnancy increases the risk of development of which of the following malformations in the baby?

- **ID:** da27e783-4c0b-4621-bc3d-938a109d8425
- **Subject/topic:** Pharmacology / AIIMS 2018
- **Gold answer:** B. Cardiac defects
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (fixed)

#### 415. All of the following carry proprioception from head and neck except:

- **ID:** d239a8a4-bc54-453e-805f-068d00381a1b
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** D. Cranial accessory nerve
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 416. What is the cause of delirium tremens in alcoholics?

- **ID:** 0d679abd-78de-4477-a322-c8ef6dca8ec2
- **Subject/topic:** Medicine / AIIMS 2019
- **Gold answer:** B. Abrupt cessation of heavy and prolonged consumption of alcohol
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 417. If the Rb gene phosphorylation is defective, which of the following will happen?

- **ID:** 07d58883-b752-4898-ab70-a1df892ef7bd
- **Subject/topic:** Pathology / unknown
- **Gold answer:** A. Cell cycle will stop at GI phase
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 418. A 2 weeks old infant has conjunctivitis, which later developed into respiratory distress and pneumonia. Chest X-ray showed bilateral lung infiltrates. WBC count was 14,300/dL. Which of the following is the most likely organism?

- **ID:** 58e40694-1799-476f-8618-af488bda8892
- **Subject/topic:** Microbiology / unknown
- **Gold answer:** A. Chlamydia trachomatis
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 419. Treatment of choice in childhood thyrotoxicosis :

- **ID:** 16b0d12a-6521-4f27-a70f-2726a7a3f6a3
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** C. Carbimazole
- **Baseline answer:** C (correct)
- **RAG k=15:** D (corrupted)

#### 420. A medical student presented to the ED with protracted vomiting. For this he was given and anti-emetic drug following which he developed abnormal posturing. Which of the following is the most likely drug to be given to the patient?

- **ID:** a022212e-e91a-4bb5-b6ff-b1fb57ff48e0
- **Subject/topic:** Medicine / AIIMS 2018
- **Gold answer:** A. Metoclopramdie
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 421. A 12-years-old boy presents with a symmetric, expansile cystic lesion in the proximal humerus. All of the following can be done for his treatment except

- **ID:** fddbb54c-e463-437d-8bd6-f48e23002637
- **Subject/topic:** Surgery / unknown
- **Gold answer:** B. Intralesional steroids
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 422. A youthful feminine smile have all the characteristics except?

- **ID:** 1e199c58-ba61-4f85-b84a-578c3f10a294
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Closure of incisor embrasure
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 423. For testing the statistical significance of the difference in heights of school children -

- **ID:** dcda3f1a-0ff7-411e-9a61-fa2b6cb8f3c3
- **Subject/topic:** Social & Preventive Medicine / unknown
- **Gold answer:** D. ANOVA
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 424. Greater crown bulk distal to the faciolingual dissecting plane of the tooth is most typical of mandibular

- **ID:** 0a08a713-9a1e-49db-99ed-d0050c717e02
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Canine
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 425. Which drug causes flagellate pigmentation of skin?

- **ID:** 13775adf-3c9f-46c4-9149-d0a382e24277
- **Subject/topic:** Pharmacology / unknown
- **Gold answer:** A. Bleomycin
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 426. Anchoring fibres of lamina densa contains:

- **ID:** 7e16d363-708e-4d43-9c1f-f80035a742ac
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Type 7 collagen.
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 427. True about Levator Ani except -

- **ID:** 436d7d2f-93e5-4a85-84b5-f4c701863126
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** D. Attached to pelvic brim
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 428. In OKC which is more aggressive and has more recurrence potential

- **ID:** 1c6cc29a-27a8-4d86-bd43-ac0c03533088
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. Parakeratinized
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 429. Rooting reflex also known as search reflex disappears:

- **ID:** 8c968c9b-35b1-4394-959a-fe3c80e283e5
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. 4 month
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 430. An individual with a known psychiatric disorder or on treatment and is not a minor can chose to decide the care taker and the course of treatment according to mental health act. This is called:

- **ID:** f361defb-1a36-496f-b195-9dcb6bb31ea5
- **Subject/topic:** Psychiatry / AIIMS 2018
- **Gold answer:** A. Advance directive
- **Baseline answer:** B (incorrect)
- **RAG k=15:** A (fixed)

#### 431. Which of the following complications of stroke need not to be treated?

- **ID:** d6a8de08-5a4c-404b-8622-217e17e5751b
- **Subject/topic:** Medicine / unknown
- **Gold answer:** B. Spasticity
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 432. Storage temperature of RBC, Platelet, and Fresh Frozen Plasma (FFP) are:

- **ID:** 97194c13-bb56-4e06-ac35-79f69cb41bb3
- **Subject/topic:** Pathology / AIIMS 2018
- **Gold answer:** A. RBC 2-6oC, Platelet 20-22oC, FFP-30oC
- **Baseline answer:** A (correct)
- **RAG k=15:** C (corrupted)

#### 433. Which type of radiation effect results in radiation induced thyroid cancer?

- **ID:** 9a21d76c-9104-4bd2-be55-a37c3b71c0f5
- **Subject/topic:** Radiology / unknown
- **Gold answer:** A. Somatic
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 434. 8 year-old child had fractured his maxillary central incisor
10-months ago. The pulp shows no response. There is no periapical lesion in the radiograph. The treatment of choice is:

- **ID:** 376472be-1031-446f-abbd-f35a14669d7f
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Complete debridement and apexification
- **Baseline answer:** D (correct)
- **RAG k=15:** C (corrupted)

#### 435. In BSSO setback, fixation in neutral posterior zone is best achieved with:

- **ID:** 80d140b3-ecea-49ed-a805-775b3f067383
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. Lag screw
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 436. A 10–year old male child was presented to the pediatrician for evaluation of a seizure disorder. On examination a vascular plaque was found along the ophthalmic and maxillary divisions of the trigeminal nerve. The mother informed the pediatrician that the lesion was present since birth and there was no change in morphology. The most likely possibility is –

- **ID:** 1d7c2dff-73e6-46d8-8d10-ab6ee7464701
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** A. Sturge Weber syndrome
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 437. Specific plaque hypothesis state that

- **ID:** a8ac17a8-7d55-4708-a9d9-fb7b1c05fe1f
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Plaque is pathogenic only when signs of associated disease are present
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 438. A patient is giving; history of avulsed tooth 20 minutes back, comes to dentist what should be done?

- **ID:** a20626b3-8719-4847-a929-87a7c9727649
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Rinse with saline and reimplant
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 439. First order neuron of visual pathway -

- **ID:** 6c84e800-14f3-4ba3-9324-84247cbae881
- **Subject/topic:** Ophthalmology / unknown
- **Gold answer:** A. Photoreceptor
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 440. Cumulative index is:

- **ID:** 66b9ec80-bfe0-485a-89ae-42e666aab572
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. PMA (Massler and Schlour)
- **Baseline answer:** D (incorrect)
- **RAG k=15:** C (fixed)

#### 441. A patient of disseminated malignancy comes to the palliative care clinic with nausea, vomiting and altered sensorium. Hypercalcemia is detected on investigations. What will be the first line of management?

- **ID:** 1f8a97a5-64cf-4635-a50a-e84ac5a0d7f1
- **Subject/topic:** Medicine / unknown
- **Gold answer:** C. Intravenous fluids
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 442. A 27 year primigravida presents with pregnancy induced hypertension with blood pressure of 150/100 mm of Hg at 32 weeks of gestation with no other complications. Subsequently, her blood pressure is controlled on treatment. If there are no complications, the pregnancy should be terminated at:

- **ID:** ca59647e-62f5-4b2e-a0fd-e85f05af60c4
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** B. 37 completed weeks
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 443. A 10 year old boy presents with midline swelling arising from cerebellum the diagnosis is –

- **ID:** 772be35c-73b9-43c4-8fc6-9ee4efb8dd27
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** D. Medulloblastoma
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 444. Anterior division of mandibular nerve has:

- **ID:** d13f2a21-04e2-4c68-9f60-d02262a7ab55
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** A. One sensory and all motor branches
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 445. Which of the following are seen in ectodermal dysplasia?

- **ID:** cb19c2ac-3ade-4f32-9a3f-64f3d6efd517
- **Subject/topic:** Pathology / unknown
- **Gold answer:** D. Any of the above
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 446. Suture technique is called as:

- **ID:** f447d416-8b56-4a22-a6bc-9b3467fc4b1d
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Figure eight suture.
- **Baseline answer:** C (correct)
- **RAG k=15:** A (corrupted)

#### 447. To establish the diagnosis of H-type trachea-esophageal fistula, which if the following is required?

- **ID:** fffb00bf-d5e6-4975-9299-12beacacb8ad
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** B. Tracheo-bronchoscopy
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (fixed)

#### 448. A 1.5 kg child born at 32 weeks by LSCS presents with moderate respiratory difficulty (RR 70/ minutes). Which of the following is the appropriate management –

- **ID:** 16533187-64d0-47f9-be71-dba4d56615fe
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** A. CPAP
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 449. HCO3/H2CO3 is the best buffer because it is:

- **ID:** 20445700-6fe0-4e44-b27c-561d580c5ea9
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** B. Its components can be increased or decreased in the body as needed
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (fixed)

#### 450. Lateral pharyngeal space is not connected directly by:

- **ID:** 2066f9f0-3eb8-4f40-8ca3-39406b885674
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. Buccal space
- **Baseline answer:** D (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 451. An affected male does not have affected children but an affected female always has affected children. Type of inheritance?

- **ID:** 87e68531-25dc-4647-a84c-28b40279d8fe
- **Subject/topic:** Pediatrics / AIIMS 2019
- **Gold answer:** D. Mitochondrial
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 452. Which of the following instrument does not have 4 digits?

- **ID:** 046ddc6f-759d-4234-b6a8-89ad6017ef3a
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Enamel hatchet
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 453. Which of the following is associated with defective apoptosis and increased cell survival

- **ID:** f23d2f9b-0dd0-49b4-88de-b7b8570ee171
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. Auto immune disorders
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (fixed)

#### 454. Calcification of roots of deciduous teeth is completed by:

- **ID:** 03072fac-4647-4c94-816b-41a3e44a72a1
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. 4 years
- **Baseline answer:** C (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 455. In genomic imprinting. DNA is modified by:

- **ID:** bf77a9c9-3c08-43fc-8159-8f8509238024
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. Methylation
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 456. FNAC can not diagnose

- **ID:** ccec60b1-80b6-4130-b1ab-8631cac2fa14
- **Subject/topic:** Surgery / unknown
- **Gold answer:** B. Follicular carcinoma of thyroid
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 457. Maximum level of alpha fetoprotein is seen in:

- **ID:** 065b4850-1738-4a30-9c3f-1fb89d9c0123
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** A. Fetal serum
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 458. A patient is undergoing MRND for laryngeal malignancy; while dissecting the venous tributaries the surgeon elevated the internal jugular vein for ligation. Suddenly the patients EtCO2 dropped from 3g mmHg to 12 mmHg and the patient developed hypotension along with cardiac arrhythmia. Which of the following is most likely cause??

- **ID:** d2198d20-fa7b-4abd-a3f6-d849ee0973fb
- **Subject/topic:** Anaesthesia / unknown
- **Gold answer:** C. Venous air embolism
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 459. Which of the following is not a content of mesorectal fascia?

- **ID:** 33b23fe7-afeb-4475-af4c-a9e250c82578
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** A. Inferior rectal vein
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 460. Median rhomboid glossitis is associated with:

- **ID:** 46fe2094-87db-4117-b06f-7a7bebb94646
- **Subject/topic:** Pathology / unknown
- **Gold answer:** D. Absence of filiform papillae
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 461. Strength of collagen is due to:

- **ID:** 1579b75c-7804-45da-b317-eb16bac036be
- **Subject/topic:** Pathology / unknown
- **Gold answer:** D. Hydroxyproline
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 462. Ratio of mesiodistal width to height of crown of maxillary canine

- **ID:** 4d48f925-c908-4543-b466-e97ff099812c
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. 8:10
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 463. VLDL is synthesised in

- **ID:** dd032c3c-d1fc-42c9-bdbf-09d5fcef74fd
- **Subject/topic:** Biochemistry / unknown
- **Gold answer:** B. Liver
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 464. Treatment of choice for erythrodermic psoriasis:

- **ID:** aa677f5e-3b2c-4ec8-8b77-78610a8a38cf
- **Subject/topic:** Skin / unknown
- **Gold answer:** A. Methotrexate
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 465. All of following are recognized manifestation of acute Rheumatic fever except –a) Abdominal painb)  Epistaxisc)  Choread)  Subcutaneous nodules

- **ID:** 810e4333-a984-4b47-821a-d6dddd1615d7
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** D. ab
- **Baseline answer:** D (correct)
- **RAG k=15:** C (corrupted)

#### 466. Cranial nerve that is not involved in olfaction:-

- **ID:** e584f190-0cb1-4ef7-9e2a-e4f0ccc8e01b
- **Subject/topic:** ENT / AIIMS 2018
- **Gold answer:** C. Hypoglossal
- **Baseline answer:** C (correct)
- **RAG k=15:** D (corrupted)

#### 467. Which of the following is not present in posterior
triangle of neck?

- **ID:** 5f2e0649-aabe-48ad-9063-2c4554d053a2
- **Subject/topic:** Anatomy / unknown
- **Gold answer:** D. Hypoglossal nerve
- **Baseline answer:** A (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 468. Which of the following structure is disrupted by Vibrio cholerae?

- **ID:** 8fe12f62-9e59-408b-899d-72def6e9e16e
- **Subject/topic:** Microbiology / unknown
- **Gold answer:** C. Zona occludens
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 469. In carrier base gutta percha the plastic carrier size of 40- 90 are made by?

- **ID:** bebb654f-88d5-4a1f-a9fb-dd65b42beeca
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Poly sulphone
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 470. Hematuria during labour in previous LSCS is sign

- **ID:** ae4e70ec-f2cc-4afa-b122-cdb5a4eede13
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** A. Impending rupture of scar
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 471. The treatment of choice for stage-I cancer larynx is:

- **ID:** 4719558d-09ca-4c85-9bf8-454e80a138aa
- **Subject/topic:** Surgery / unknown
- **Gold answer:** C. Radiotherapy
- **Baseline answer:** D (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 472. A politician is shot in the back during a rally at level of T8 veebral immediately after the shot he loses all the sensation below level of lesion. Chance of regeneration of spinal cord due to the fact that injured nerve is not able to regenerate is due to reason all except:

- **ID:** 1a9cdc6b-3c9c-44a2-95d1-68461bf113fc
- **Subject/topic:** Physiology / unknown
- **Gold answer:** D. Lack of myelin inhibiting substance
- **Baseline answer:** D (correct)
- **RAG k=15:** B (corrupted)

#### 473. Porcelain denture teeth

- **ID:** f9b91625-8627-40e9-ae62-e7085acb8f3a
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Have a higher abrasion resistance than gold
- **Baseline answer:** C (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 474. In extraction, best time to administer analgesics is:

- **ID:** fa7ee43b-5ca6-4b65-a72d-9bafd53b25df
- **Subject/topic:** Surgery / unknown
- **Gold answer:** A. Before anaesthesia wears off
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 475. Modulus of elasticity of which cement is best to support under complex amalgam restoration?

- **ID:** 119b2538-3a82-4ed2-94bc-50e807b9545e
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. ZnPO4
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (fixed)

#### 476. In full tooth borne dentures occlusal rests transmits _________ percentage of occlusal forces to teeth:

- **ID:** de4374af-70ba-41e4-b46a-5159e73a690e
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. 100%
- **Baseline answer:** D (correct)
- **RAG k=15:** D (preserved_correct)

#### 477. Scaphocephaly is caused by premature fusion of:

- **ID:** b9430ce6-2167-41f1-86a6-5d8c3e143d86
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. Sagittal suture
- **Baseline answer:** C (incorrect)
- **RAG k=15:** B (fixed)

#### 478. A case presented with lower natural teeth and 7 maxillary implants placed,  having space of 15 mm for the restoration. What would be the ideal treatment plan  for the patient?

- **ID:** 5ef662e7-6d00-4ca1-a592-b862a54a5efa
- **Subject/topic:** Dental / unknown
- **Gold answer:** D. Hybrid denture
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 479. Which one of the following is the role of barrier membrane in GTR?

- **ID:** 6a86faf5-cc79-438b-b82f-53839e1ce3ab
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Prevention of epithelial migration
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 480. Characteristics radiological feature of transient tachypnoea of newborn is –

- **ID:** e8b34af9-6a4b-42cf-90ce-fb46a23db79d
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** C. Prominent horizontal fissure
- **Baseline answer:** A (incorrect)
- **RAG k=15:** D (preserved_incorrect)

#### 481. A 46 years old male patient was given subarachnoid block with bupivacaine (heavy) by the anesthetist. After 10 minutes he was found to have a BP of 72/44 mm Hg and hea rate of 52/min. On checking the level of block it was found to be T6. What is the likely explanation for the bradvcardia?

- **ID:** 930d4945-04ef-4c32-9c9d-279e8226f852
- **Subject/topic:** Anaesthesia / unknown
- **Gold answer:** A. Bezold-Jarisch reflex
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 482. Which type of oral candidiasis does not presents with white patch?

- **ID:** f6bb3faa-6ccb-4838-a2d9-1ae2f2d63e7d
- **Subject/topic:** Skin / unknown
- **Gold answer:** A. Chronic atrophic candidiasis
- **Baseline answer:** D (incorrect)
- **RAG k=15:** A (fixed)

#### 483. Which of the following diseases is NOT transmitted by it?

- **ID:** 8be0f11a-fb38-4996-95b7-b3fcf36de7c4
- **Subject/topic:** Social & Preventive Medicine / AIIMS 2019
- **Gold answer:** C. Babesiosis
- **Baseline answer:** D (incorrect)
- **RAG k=15:** C (fixed)

#### 484. Not a side effect of Escitalopram?

- **ID:** 5a2f9e25-3acb-4830-9f18-009480595be1
- **Subject/topic:** Psychiatry / AIIMS 2019
- **Gold answer:** D. Sialorrhoea
- **Baseline answer:** B (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 485. A 16 years old girl walks into your clinics and asks for Ca cervix vaccination.Which of the following should be administered?

- **ID:** 7bb29056-c6b1-4d7b-b513-e6eab45eeb86
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** A. Gardasil 9
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 486. Steepest cusp is seen in:

- **ID:** cb8ea9a3-b993-4d69-a1e2-aa031b0bdb11
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. Maxillary 1st premolar
- **Baseline answer:** D (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 487. Which marker shows holocrine gland?

- **ID:** b3163789-82b3-4054-aabe-3a2b90aa7a98
- **Subject/topic:** Anatomy / AIIMS 2017
- **Gold answer:** A. A
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 488. Brachytherapy is:

- **ID:** 0ba9328b-c265-4d98-8259-314789a2f00d
- **Subject/topic:** Pathology / unknown
- **Gold answer:** C. Irradiation of tissues by implants within the tissues
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 489. Dengue discharge protocol includes

- **ID:** fb47f171-c6d7-4871-8d28-92f2b97acc88
- **Subject/topic:** Social & Preventive Medicine / AIIMS 2019
- **Gold answer:** D. Return of normal appetite
- **Baseline answer:** C (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 490. Which of the following is most common location of intracranial neurocysticercoses:

- **ID:** bd0ed5fa-d212-4dfc-bba3-9706fe6a228d
- **Subject/topic:** Pathology / unknown
- **Gold answer:** A. Brain parenchyma
- **Baseline answer:** A (correct)
- **RAG k=15:** A (preserved_correct)

#### 491. Acid dissolution is most common in which part of rod

- **ID:** a67293d8-42a6-4fe5-a2ac-ee22bc9ebaf9
- **Subject/topic:** Dental / unknown
- **Gold answer:** B. Head region
- **Baseline answer:** C (incorrect)
- **RAG k=15:** C (preserved_incorrect)

#### 492. Most common presentation of abdominal desmoids tumor is?

- **ID:** ed111e74-8d76-4f2f-ac59-56e7ddc2be88
- **Subject/topic:** Surgery / AIIMS 2017
- **Gold answer:** B. Abdominal mass
- **Baseline answer:** B (correct)
- **RAG k=15:** B (preserved_correct)

#### 493. 26 years old female suffers from PPH on her second postnatal day. Her APTT and PTT are prolonged while BT, PT and platelet counts are normal. Likely diagnosis is:

- **ID:** eaae5960-af00-46cd-8bf6-2b238919fb76
- **Subject/topic:** Gynaecology & Obstetrics / unknown
- **Gold answer:** A. Acquired hemophilia
- **Baseline answer:** B (incorrect)
- **RAG k=15:** B (preserved_incorrect)

#### 494. Biomarker of alcoholic hepatitis:

- **ID:** 7ee6d817-eee3-42ad-8d49-7237f375f6f3
- **Subject/topic:** Biochemistry / AIIMS 2018
- **Gold answer:** D. GGT
- **Baseline answer:** D (correct)
- **RAG k=15:** B (corrupted)

#### 495. All are drugs which lower IOP except

- **ID:** 065971a5-7b85-4a6d-a657-8d152956f946
- **Subject/topic:** Ophthalmology / AIIMS 2019
- **Gold answer:** C. Dexamethasone
- **Baseline answer:** B (incorrect)
- **RAG k=15:** C (fixed)

#### 496. Which of following in not true about SLE?

- **ID:** 36fbf017-4fe4-4eb2-b6e8-5cd677d31a5d
- **Subject/topic:** Pathology / unknown
- **Gold answer:** B. ROR-2 gene mutation
- **Baseline answer:** A (incorrect)
- **RAG k=15:** A (preserved_incorrect)

#### 497. Condensation reaction occurs in

- **ID:** 98035f50-53b3-47c8-b340-392237162fb2
- **Subject/topic:** Dental / unknown
- **Gold answer:** C. Polysulfide
- **Baseline answer:** C (correct)
- **RAG k=15:** B (corrupted)

#### 498. White patch is seen on the buccal mucosa consisting of
pseudomycelium and chalmydospores with desquamated
epithelium adjacent to it, the patient is suffering from

- **ID:** b8647a35-334f-4fda-a718-cd7f59d90d8d
- **Subject/topic:** Pathology / unknown
- **Gold answer:** C. candidiasis
- **Baseline answer:** C (correct)
- **RAG k=15:** C (preserved_correct)

#### 499. Absence of which of the following milestone in 3 yr old chitd is called delayed development?

- **ID:** 1fe1bd49-93cd-4bea-8beb-fdf6cc819421
- **Subject/topic:** Pediatrics / unknown
- **Gold answer:** C. Feeding by spoon
- **Baseline answer:** A (incorrect)
- **RAG k=15:** C (fixed)

#### 500. Percentage of Phosphoric acid where Dicalcium phosphate
monohydrate is formed that cannot be rinsed off.

- **ID:** 1e6d84fb-a062-4394-803a-d7466fc8cd83
- **Subject/topic:** Dental / unknown
- **Gold answer:** A. 25%
- **Baseline answer:** B (incorrect)
- **RAG k=15:** D (preserved_incorrect)

---
