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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-102MS` (url=291ms, nekobox=313ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-108MS` (url=295ms, nekobox=335ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-115MS` (url=282ms, nekobox=506ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-115MS` (url=292ms, nekobox=313ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-110MS` (url=289ms, nekobox=329ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-123MS` (url=273ms, nekobox=311ms, status=yes)
7. `AKUN-007-UK-GB-DCL-01-20191003-VLESS-WS-125MS` (url=309ms, nekobox=342ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-133MS` (url=307ms, nekobox=339ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-125MS` (url=293ms, nekobox=302ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-147MS` (url=277ms, nekobox=323ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-142MS` (url=313ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-150MS` (url=293ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-148MS` (url=300ms, status=HTTP 204)
14. `AKUN-014-PAGES-VLESS-WS-149MS` (url=355ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-174MS` (url=294ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-194MS` (url=347ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-172MS` (url=324ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-247MS` (url=434ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-293MS` (url=580ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-324MS` (url=2692ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-327MS` (url=698ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-347MS` (url=722ms, status=HTTP 204)
23. `AKUN-024-SE-FORNEX-VLESS-WS-527MS` (url=960ms, status=HTTP 204)
24. `AKUN-025-WPENG-VLESS-WS-136MS` (url=300ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-534MS` (url=827ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
