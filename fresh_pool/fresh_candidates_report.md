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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-93MS` (url=282ms, nekobox=331ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-100MS` (url=290ms, nekobox=343ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-114MS` (url=276ms, nekobox=326ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-79MS` (url=293ms, nekobox=332ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-108MS` (url=273ms, nekobox=443ms, status=yes)
6. `AKUN-006-WPENG-VLESS-WS-118MS` (url=368ms, nekobox=338ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-122MS` (url=334ms, nekobox=313ms, status=yes)
8. `AKUN-008-GO-DADDY-COM-LLC-VLESS-WS-104MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-108MS`
10. `AKUN-010-466688-VLESS-WS-131MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-121MS` (url=314ms, status=HTTP 204)
12. `AKUN-013-UNKNOWN-VLESS-WS-116MS` (url=301ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-137MS` (url=316ms, status=HTTP 204)
14. `AKUN-015-DIXONS-VLESS-WS-150MS` (url=308ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-124MS` (url=299ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-119MS` (url=357ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-136MS` (url=362ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-145MS` (url=325ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-163MS` (url=299ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-123MS` (url=318ms, status=HTTP 204)
21. `AKUN-022-ZVC-VLESS-WS-122MS` (url=347ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-321MS` (url=648ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-330MS` (url=666ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-333MS` (url=2832ms, status=HTTP 204)
25. `AKUN-026-INTERNETWORKS-45-131-210-VLESS-WS-352MS` (url=683ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
