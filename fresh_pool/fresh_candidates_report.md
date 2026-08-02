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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=232ms, nekobox=246ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-59MS` (url=237ms, nekobox=250ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-63MS` (url=244ms, nekobox=174ms, status=no)
4. `AKUN-003-UNKNOWN-VLESS-WS-66MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-63MS` (url=257ms, nekobox=172ms, status=no)
6. `AKUN-004-OVH-VLESS-WS-60MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-66MS` (url=235ms, nekobox=174ms, status=no)
8. `AKUN-005-CLOUDFLARE-VLESS-WS-67MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-71MS` (url=258ms, nekobox=177ms, status=no)
10. `AKUN-006-CLOUDFLARE-VLESS-WS-63MS`
11. `AKUN-007-UNKNOWN-VLESS-WS-80MS`
12. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS`
13. `AKUN-009-090227-VLESS-WS-99MS`
14. `AKUN-010-UNKNOWN-VLESS-WS-85MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-61MS` (url=265ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-122MS` (url=259ms, status=HTTP 204)
17. `AKUN-017-DE-CLOUDKLEYER-20190515-VLESS-WS-115MS` (url=322ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-140MS` (url=276ms, status=HTTP 204)
19. `AKUN-019-FASTVPSUS-IPV4-VLESS-WS-116MS` (url=354ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-64MS` (url=237ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-360MS` (url=676ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-372MS` (url=727ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-411MS` (url=530ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-369MS` (url=726ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-451MS` (url=780ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
