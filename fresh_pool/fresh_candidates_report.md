# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-UNKNOWN-VLESS-WS-70MS` (url=215ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-80MS` (url=221ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-116MS` (url=290ms, nekobox=253ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS` (url=228ms, nekobox=242ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS` (url=204ms, nekobox=251ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-94MS` (url=249ms, nekobox=185ms, status=no)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-91MS` (url=219ms, nekobox=225ms, status=no)
8. `AKUN-006-BROADNNET-KR-VLESS-WS-159MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-89MS` (url=226ms, nekobox=202ms, status=no)
10. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-140MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-193MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-250MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-266MS`
14. `AKUN-014-MICROSOFT-VLESS-WS-269MS` (url=593ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-260MS` (url=644ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-268MS` (url=560ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-264MS` (url=503ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-267MS` (url=552ms, status=HTTP 204)
19. `AKUN-025-UNKNOWN-VLESS-WS-498MS` (url=684ms, status=HTTP 204)
20. `AKUN-027-RS-RAPIDSEEDBOX-20190717-VLESS-WS-502MS` (url=802ms, status=HTTP 204)
21. `AKUN-029-VIDBOXCO-VLESS-WS-526MS` (url=727ms, status=HTTP 204)
22. `AKUN-030-VIDBOXCO-VLESS-WS-504MS` (url=721ms, status=HTTP 204)
23. `AKUN-031-VIDBOXCO-VLESS-WS-511MS` (url=718ms, status=HTTP 204)
24. `AKUN-032-VIDBOXCO-VLESS-WS-532MS` (url=769ms, status=HTTP 204)
25. `AKUN-033-VIDBOXCO-VLESS-WS-513MS` (url=784ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
