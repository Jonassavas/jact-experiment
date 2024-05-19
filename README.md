# JACT-experiment

_This repository contains the summaries for all the results evaluating [JACT](https://github.com/Jonassavas/jact). The complete JACT reports for all projects can be downloaded as a 450MB .zip file [here](https://drive.google.com/file/d/1YZoDyiZ2mMbWXHAgPkl9frnX3LRZedZ6/view?usp=drive_link). The results contain 30 open-source Java projects chosen for their compatability and relevance with related work, [DepTrim](https://arxiv.org/abs/2302.08370)._


---
#### [Checkstyle:](https://github.com/checkstyle/checkstyle)  
- Commit: [dbeb902](https://github.com/checkstyle/checkstyle/commit/dbeb9024c861ad11b194e40d8c6e08d7e6ec5122)  
- [JACT-Report](./checkstyle_jact-report/)
- #Tests: 3887
---

#### [Chronicle-Map:](https://github.com/OpenHFT/Chronicle-Map)
- Commit: [608c6f9](https://github.com/OpenHFT/Chronicle-Map/commit/608c6f9d1c8560522ead73aca856d994690e5c46) LATEST RELEASE (NOT DEPTRIM)
- [JACT-Report](./chronicle-map_jact-report/)
- #Tests: 1291 (73 Skipped)
---


#### [classgraph:](https://github.com/classgraph/classgraph)  
- Commit: [92b6446](https://github.com/classgraph/classgraph/commit/92b644677964496fb841ba41bed52247f8a24786)  
- [JACT-Report](./classgraph_jact-report/)  
Note: Had to remove two tests for JaCoCo to work in classgraph/src/test/java/io/github/classgraph/issues/DeclaredVsNonDeclaredTest.java ; negligible impact on coverage
`publicAndPrivateDeclaredVsNonDeclared()`  
`publicDeclaredVsNonDeclared()`
- #Tests: 168 (Skipped 2)
---

#### [commons-validator:](https://github.com/apache/commons-validator)
- Commit: [f9bb217](https://github.com/apache/commons-validator/commit/f9bb21748a9f9c50fbc31862de25ed49433ecc88)  
- [JACT-Report](./commons-validator_jact-report/)
- #Tests: 576 (Skipped 1)

---
#### [CoreNLP:](https://github.com/stanfordnlp/CoreNLP)  LATEST RELEASE (NOT DEPTRIM) Faulty commit link on deptrim
- Commit: [2460079](https://github.com/stanfordnlp/CoreNLP/commit/246007929ca8461804d2241b5b3ccbc9897eb1bd)  
- [JACT-Report](./corenlp_jact-report/)
- #Tests: 1459

---
#### [flink:](https://github.com/apache/flink)  
- Commit: [eaffd22](https://github.com/apache/flink/commit/eaffd227d853e0cdef03f1af5016e00f950930a9)  
- [JACT-Report](./flink-flink-java_jact-report/)
- Module: flink-java
- #Tests: 855 (38 skipped)

---
#### [Graphhopper:](https://github.com/graphhopper/graphhopper)  
- Commit: [6d3da379](https://github.com/graphhopper/graphhopper/commit/6d3da37960f56aa6b9c4b1ffd77f70ebebff8747)  
- [JACT-Report](./graphhopper-core_jact-report/)
- Module: core
- #Tests: 2460 (29 skipped)

---
#### [guice:](https://github.com/google/guice)
- Commit: [b0ff10c](https://github.com/google/guice/commit/b0ff10c8ec8911137451623a333d6daa65f73d8a)
- [JACT-Report](./guice-core_jact-report/)
- #Tests: 979

---
#### [helidon:](https://github.com/helidon-io/helidon)
- Commit: [99cf5ad](https://github.com/helidon-io/helidon/commit/99cf5add9b4049581f08aae9eddaf0280070f2bb)
- [JACT-Report](./helidon-openapi_jact-report/)
- Module: openapi
- #Tests: 30

---
#### [httpcomponents-client:](https://github.com/apache/httpcomponents-client)
- Commit: [d8f702f](https://github.com/apache/httpcomponents-client/commit/d8f702fb4d44c746bb0edf00643aa7139cb8bdf7)
- [JACT-Report](./httpcomponents-client-httpclient5_jact-report/)
- Module: httpclient5
- #Tests: 669

---
#### [immutables:](https://github.com/immutables/immutables)
- Commit: [6e19203](https://github.com/immutables/immutables/commit/6e192030320eaf7a8b5f146c39ae5a17b413aa37)
- [JACT-Report](./immutables-gson_jact-report/)
- Module: gson
- #Tests: 37

---
#### [jacop:](https://github.com/radsz/jacop)
- Commit: [1a395e6](https://github.com/radsz/jacop/commit/1a395e6add22caf79590fe9d1b2223bfb6ed0cd0)
- [JACT-Report](./jacop_jact-report/)
- #Tests: 210 (2 Skipped)

---
#### [java-faker:](https://github.com/DiUS/java-faker)
- Commit: [e23d606](https://github.com/DiUS/java-faker/commit/e23d6067c8f83b335a037d24e6107a37eb0b9e6e)
- [JACT-Report](./java-faker_jact-report/)
- #Tests: 500

---
#### [jcabi-github:](https://github.com/jcabi/jcabi-github)
- Commit: [02f3ab9](https://github.com/jcabi/jcabi-github/commit/02f3ab93156349c2f66989ac675bd6292462d724)
- [JACT-Report](./jcabi-github_jact-report/)
- #Tests: 83 (Skipped 80)

---
#### [jimfs:](https://github.com/google/jimfs)
- Commit: [3bc54fa](https://github.com/google/jimfs/commit/3bc54fae2feb218dcf5427d2626720fc09ef38d1)
- [JACT-Report](./jimfs-jimfs_jact-report/)
- Module: jimfs
- #Tests: 5893

---
#### [jooby:](https://github.com/jooby-project/jooby) DID NOT WORK YET
- Commit: [4d7be54](https://github.com/jooby-project/jooby/commit/4d7be54dad429b5aeb5266387df14b0781c78357)
- [JACT-Report](./jooby_jact-report/)
- Module: jooby
- #Tests: 122

---
#### [lettuce:](https://github.com/redis/lettuce)
- Commit: [77c4ea](https://github.com/redis/lettuce/commit/77c4ea587fdba73f688c95a481d2743b6fc94fcb)
- [JACT-Report](./lettuce-core_jact-report/)
- Module: core
- #Tests: 2600 (Skipped 1)

---
#### [modelmapper:](https://github.com/modelmapper/modelmapper)
- Commit: [894c658](https://github.com/modelmapper/modelmapper/commit/894c658609f47f817ce20e41f6e87e1f803663ee)
- [JACT-Report](./modelmapper-core_jact-report/)
- Module: core
- #Tests: 614

---
#### [mybatis-3:](https://github.com/mybatis/mybatis-3) LATEST
- Commit: [78bb677](https://github.com/mybatis/mybatis-3/commit/78bb677e2bf04b43386d3f1544cec51ff47662a2)
- [JACT-Report](./mybatis-3_jact-report/)
- #Tests: 1790 (Skipped 19)

---
#### [OpenPDF:](https://github.com/LibrePDF/OpenPDF)
- Commit: [0c9c4ca](https://github.com/LibrePDF/OpenPDF/commit/0c9c4ca393b01444b7cb13bb1d12da202bd0d458)
- [JACT-Report](./openpdf-openpdf_jact-report/)
- Module: openpdf
- #Tests: 35

---

#### [pdfbox:](https://github.com/apache/pdfbox)  LATEST
- Commit: [9a1fc84](https://github.com/apache/pdfbox/commit/9a1fc842799d6a4a1e9df33b0f3ebc687294935f)  
- [JACT-Report](./pdfbox-pdfbox_jact-report/)
- #Tests: 624
- Manually excluded a test that was excluded by surefire:
    - "./pdfbox/pdfbox/src/test/java/org/apache/pdfbox/rendering/TestPDFToImage.java/testRenderImage()"

---
#### [pf4j:](https://github.com/pf4j/pf4j)
- Commit: [efaed93](https://github.com/pf4j/pf4j/commit/efaed93c10dd9d114335e2a344e8bca04fd00c63)
- [JACT-Report](./pf4j-pf4j_jact-report/)
- Module: pf4j
- #Tests: 151

---
#### [poi-tl:](https://github.com/Sayi/poi-tl)
- Commit: [5d50043](https://github.com/Sayi/poi-tl/commit/5d5004311a406b7d5843be76322bf208071b5969)
- [JACT-Report](./poi-tl_jact-report/)
- #Tests: 125

---
#### [Recaf:](https://github.com/Col-E/Recaf)
- Commit: [c66f238](https://github.com/Col-E/Recaf/commit/c66f23801493bd866db757b0594c1fceaa30dce0)
- [JACT-Report](./recaf_jact-report/)
- #Tests: 274 (Skipped 1)

---
#### [RxRelay:](https://github.com/JakeWharton/RxRelay)
- Commit: [e9fc158](https://github.com/JakeWharton/RxRelay/commit/e9fc1586192ca1ecdbc41ae39036cbf0d09428b5)
- [JACT-Report](./rxrelay_jact-report/)
- #Tests: 64 (Skipped 3)

---
#### [scribejava:](https://github.com/scribejava/scribejava)
- Commit: [763a959](https://github.com/scribejava/scribejava/commit/763a959f7b05ba5b9d3dabb39c8cd6511299c419)
- [JACT-Report](./scribejava-core_jact-report/)
- Module: scribejava-core
- #Tests: 82

---
#### [tablesaw:](https://github.com/jtablesaw/tablesaw)
- Commit: [05823f6](https://github.com/jtablesaw/tablesaw/commit/05823f66246ea191e62ad0658d2fed0b080d5334)
- [JACT-Report](./tablesaw-json_jact-report/)
- Module: json
- #Tests: 9

---
#### [tika:](https://github.com/apache/tika)
- Commit: [41319f3](https://github.com/apache/tika/commit/41319f3c294b13de5342a80570b4540f7dd04a3e)
- [JACT-Report](./tika-core_jact-report/)
- Module: tika-core
- #Tests: 305 (Skipped 2)

---
#### [undertow:](https://github.com/undertow-io/undertow) LATEST
- Commit: [2b13a06](https://github.com/undertow-io/undertow/commit/2b13a067463a9cf60365db7c30e3f127737d0ed9)
- [JACT-Report](./undertow-core_jact-report/)
- Manually skipped 1 failing test: "undertow/core/src/test/java/io/undertow/server/handlers/file/FileHandlerIndexTestCase.java/testDirectoryIndex()"
- Module: core
- #Tests: 725 (Skipped 20)

---
#### [woodstox:](https://github.com/FasterXML/woodstox)
- Commit: [e8f0040](https://github.com/FasterXML/woodstox/commit/e8f00401bebd103f62d51383ef53da2cd58bd89e)
- [JACT-Report](./woodstox-jact-report/)
- #Tests: 868
