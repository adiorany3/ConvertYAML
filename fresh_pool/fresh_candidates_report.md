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
1. `AKUN-001-UNKNOWN-VLESS-WS-54MS` (url=212ms, nekobox=237ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-55MS` (url=212ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-56MS` (url=208ms, nekobox=235ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-56MS` (url=209ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-55MS` (url=209ms, nekobox=254ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-57MS` (url=214ms, nekobox=237ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-59MS` (url=224ms, nekobox=235ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-66MS` (url=225ms, nekobox=251ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-70MS` (url=211ms, nekobox=243ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-70MS` (url=217ms, nekobox=236ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-57MS` (url=219ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-57MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-92MS` (url=209ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-80MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-60MS` (url=225ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-85MS` (url=213ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-89MS` (url=230ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-91MS` (url=218ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-95MS` (url=211ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-102MS` (url=225ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-142MS` (url=231ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-146MS` (url=266ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-138MS` (url=307ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-340MS` (url=883ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-345MS` (url=5014ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
