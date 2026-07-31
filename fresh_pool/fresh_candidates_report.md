# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-UNKNOWN-VLESS-WS-56MS` (url=217ms, nekobox=238ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-59MS` (url=219ms, nekobox=247ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-72MS` (url=210ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS` (url=207ms, nekobox=240ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-59MS` (url=218ms, nekobox=239ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-88MS` (url=207ms, nekobox=244ms, status=yes)
7. `AKUN-007-OPENAI-VLESS-WS-70MS` (url=211ms, nekobox=240ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-67MS` (url=215ms, nekobox=246ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-106MS` (url=209ms, nekobox=252ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-114MS` (url=220ms, nekobox=258ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-84MS` (url=202ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-70MS` (url=217ms, status=HTTP 204)
13. `AKUN-015-090227-VLESS-WS-283MS` (url=582ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-376MS` (url=708ms, status=HTTP 204)
15. `AKUN-021-CLOUDFLARE-VLESS-WS-556MS` (url=818ms, status=HTTP 204)
16. `AKUN-022-CLOUDFLARE-VLESS-WS-650MS` (url=1117ms, status=HTTP 204)
17. `AKUN-023-CLOUDFLARE-VLESS-WS-596MS` (url=1012ms, status=HTTP 204)
18. `AKUN-024-CLOUDFLARE-VLESS-WS-680MS` (url=1071ms, status=HTTP 204)
19. `AKUN-025-CLOUDFLARE-VLESS-WS-528MS` (url=829ms, status=HTTP 204)
20. `AKUN-026-UNKNOWN-VLESS-WS-711MS` (url=1132ms, status=HTTP 204)
21. `AKUN-028-CLOUDFLARE-VLESS-WS-755MS` (url=1245ms, status=HTTP 204)
22. `AKUN-032-CLOUDFLARE-VLESS-WS-692MS` (url=1199ms, status=HTTP 204)
23. `AKUN-034-UNKNOWN-VLESS-WS-783MS` (url=1477ms, status=HTTP 204)
24. `AKUN-035-CLOUDFLARE-VLESS-WS-849MS` (url=1435ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
