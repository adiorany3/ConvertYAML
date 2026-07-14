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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=265ms, nekobox=313ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=245ms, nekobox=312ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=253ms, nekobox=289ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=252ms, nekobox=291ms, status=yes)
5. `AKUN-005-OVH-VLESS-WS-88MS` (url=323ms, nekobox=292ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-95MS` (url=359ms, nekobox=282ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS` (url=284ms, nekobox=310ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-100MS` (url=288ms, nekobox=292ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-88MS` (url=253ms, nekobox=283ms, status=yes)
10. `AKUN-010-IDC-SG-VLESS-WS-106MS` (url=281ms, nekobox=284ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-84MS` (url=284ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-89MS` (url=276ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-122MS` (url=267ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-80MS` (url=257ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-122MS` (url=303ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-123MS` (url=264ms, status=HTTP 204)
17. `AKUN-017-CZ-LOTUNA-19970206-VLESS-WS-84MS` (url=284ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-122MS` (url=256ms, status=HTTP 204)
19. `AKUN-019-DIXONS-VLESS-WS-116MS` (url=284ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-122MS` (url=275ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-157MS` (url=268ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-80MS` (url=264ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-131MS` (url=271ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-289MS` (url=729ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-282MS` (url=3134ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
