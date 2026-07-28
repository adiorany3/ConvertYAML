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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-52MS` (url=212ms, nekobox=252ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-61MS` (url=221ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-60MS` (url=231ms, nekobox=252ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-58MS` (url=223ms, nekobox=259ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-62MS` (url=230ms, nekobox=242ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-65MS` (url=221ms, nekobox=253ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-55MS` (url=213ms, nekobox=238ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-59MS` (url=213ms, nekobox=238ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-60MS` (url=290ms, nekobox=235ms, status=yes)
10. `AKUN-010-DEV-VLESS-WS-67MS` (url=216ms, nekobox=246ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-62MS` (url=211ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-62MS` (url=205ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-61MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-69MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-82MS` (url=224ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-64MS` (url=204ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-61MS` (url=222ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-69MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-74MS` (url=220ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-70MS` (url=198ms, status=HTTP 204)
21. `AKUN-021-SKK-VLESS-WS-76MS` (url=224ms, status=HTTP 204)
22. `AKUN-022-CCWU-VLESS-WS-59MS` (url=212ms, status=HTTP 204)
23. `AKUN-023-MEDIUM-VLESS-WS-84MS` (url=226ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-84MS` (url=203ms, status=HTTP 204)
25. `AKUN-025-ADF-VLESS-WS-84MS` (url=227ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
