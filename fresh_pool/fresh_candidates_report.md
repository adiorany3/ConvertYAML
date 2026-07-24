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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=234ms, nekobox=252ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=200ms, nekobox=228ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=220ms, nekobox=236ms, status=yes)
4. `AKUN-004-MYBB-VLESS-WS-71MS` (url=219ms, nekobox=245ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=222ms, nekobox=243ms, status=yes)
6. `AKUN-006-DEV-VLESS-WS-78MS` (url=222ms, nekobox=182ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-70MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-77MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-70MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-84MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-76MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-83MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-81MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-106MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-70MS` (url=208ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-83MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-87MS` (url=211ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-98MS` (url=199ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-78MS` (url=215ms, status=HTTP 204)
20. `AKUN-020-ZVC-VLESS-WS-80MS` (url=207ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-103MS` (url=234ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-86MS` (url=233ms, status=HTTP 204)
23. `AKUN-023-1PASSWORD-VLESS-WS-115MS` (url=227ms, status=HTTP 204)
24. `AKUN-024-MEDIUM-VLESS-WS-103MS` (url=224ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-140MS` (url=234ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
