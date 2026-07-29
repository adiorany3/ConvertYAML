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
1. `AKUN-001-UNKNOWN-VLESS-WS-57MS` (url=208ms, nekobox=234ms, status=yes)
2. `AKUN-002-ZOOM-VLESS-WS-56MS` (url=211ms, nekobox=226ms, status=yes)
3. `AKUN-003-LEVIKOGJGFDD-VLESS-WS-68MS` (url=199ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=201ms, nekobox=221ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-58MS` (url=200ms, nekobox=224ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=207ms, nekobox=239ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-66MS` (url=199ms, nekobox=231ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-77MS` (url=212ms, nekobox=225ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS` (url=216ms, nekobox=229ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-86MS` (url=200ms, nekobox=224ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-96MS` (url=209ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-100MS` (url=197ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-120MS` (url=312ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-143MS` (url=216ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-143MS` (url=222ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-136MS` (url=214ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-83MS` (url=224ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-147MS` (url=258ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-82MS` (url=203ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-149MS` (url=219ms, status=HTTP 204)
21. `AKUN-022-LEVIKOGJGFDD-VLESS-WS-200MS` (url=255ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-102MS` (url=214ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-223MS` (url=485ms, status=HTTP 204)
24. `AKUN-028-ZABIDAT-VLESS-WS-453MS` (url=1698ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-467MS` (url=980ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
