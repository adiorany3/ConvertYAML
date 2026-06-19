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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=221ms, nekobox=243ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=316ms, nekobox=245ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-69MS` (url=204ms, nekobox=243ms, status=yes)
4. `AKUN-004-MEDIUM-VLESS-WS-68MS` (url=228ms, nekobox=253ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=228ms, nekobox=242ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS` (url=222ms, nekobox=243ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=253ms, nekobox=247ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=228ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=239ms, nekobox=235ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-77MS` (url=237ms, nekobox=239ms, status=yes)
11. `AKUN-011-CLOUDWEBMANAGE-EU-FR-VLESS-WS-110MS` (url=221ms, status=HTTP 204)
12. `AKUN-012-156-246-89-0-156-246-89-VLESS-WS-85MS` (url=221ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-115MS` (url=233ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-127MS` (url=205ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-80MS` (url=201ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-119MS` (url=242ms, status=HTTP 204)
18. `AKUN-018-ADF-VLESS-WS-77MS` (url=215ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-71MS` (url=215ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-378MS` (url=796ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-384MS` (url=856ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-447MS` (url=2537ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-433MS` (url=799ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-511MS` (url=983ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-388MS` (url=819ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
