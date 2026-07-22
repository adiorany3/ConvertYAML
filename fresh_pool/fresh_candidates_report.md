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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=199ms, nekobox=232ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-66MS` (url=211ms, nekobox=231ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=204ms, nekobox=240ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-75MS` (url=202ms, nekobox=241ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-68MS` (url=221ms, nekobox=238ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-70MS` (url=213ms, nekobox=240ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-74MS` (url=207ms, nekobox=247ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-75MS` (url=233ms, nekobox=235ms, status=yes)
9. `AKUN-009-ZOOM-VLESS-WS-65MS` (url=206ms, nekobox=226ms, status=yes)
10. `AKUN-010-ORG-VLESS-WS-69MS` (url=228ms, nekobox=243ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-76MS` (url=233ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-79MS` (url=203ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-82MS` (url=284ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-71MS` (url=214ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-76MS` (url=214ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-87MS` (url=217ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-70MS` (url=210ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-79MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-105MS` (url=213ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-107MS` (url=203ms, status=HTTP 204)
21. `AKUN-021-SPEEDTEST-VLESS-WS-104MS` (url=228ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-81MS` (url=220ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-92MS` (url=211ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-75MS` (url=221ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-119MS` (url=219ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
