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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-55MS` (url=216ms, nekobox=249ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-56MS` (url=211ms, nekobox=244ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-58MS` (url=227ms, nekobox=237ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-58MS` (url=213ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-60MS` (url=211ms, nekobox=258ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-59MS` (url=213ms, nekobox=238ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-61MS` (url=209ms, nekobox=247ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-58MS` (url=218ms, nekobox=244ms, status=yes)
9. `AKUN-009-SKK-VLESS-WS-64MS` (url=218ms, nekobox=220ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-63MS` (url=210ms, nekobox=236ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-84MS` (url=219ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-70MS` (url=212ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-59MS` (url=210ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-105MS` (url=212ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-121MS` (url=218ms, status=HTTP 204)
16. `AKUN-017-ZVC-VLESS-WS-105MS` (url=223ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-93MS` (url=220ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-81MS` (url=212ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-67MS` (url=212ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-118MS` (url=243ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-321MS` (url=718ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-324MS` (url=706ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-337MS` (url=749ms, status=HTTP 204)
24. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-333MS` (url=749ms, status=HTTP 204)
25. `AKUN-026-CN-CF-VLESS-WS-410MS` (url=891ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
