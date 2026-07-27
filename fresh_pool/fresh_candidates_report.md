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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=211ms, nekobox=237ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-76MS` (url=209ms, nekobox=254ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=222ms, nekobox=245ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=214ms, nekobox=255ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=215ms, nekobox=254ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-81MS` (url=221ms, nekobox=250ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-74MS` (url=219ms, nekobox=247ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-83MS` (url=218ms, nekobox=243ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS` (url=224ms, nekobox=255ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-87MS` (url=221ms, nekobox=251ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-84MS` (url=224ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-74MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-114MS` (url=230ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-101MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-83MS` (url=206ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-101MS` (url=207ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-114MS` (url=231ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-77MS` (url=216ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-98MS` (url=219ms, status=HTTP 204)
20. `AKUN-020-ZVC-VLESS-WS-129MS` (url=229ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-160MS` (url=279ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-81MS` (url=217ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-82MS` (url=315ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-230MS` (url=584ms, status=HTTP 204)
25. `AKUN-025-NET-141-11-202-0-23-VLESS-WS-236MS` (url=487ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
