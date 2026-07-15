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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=198ms, nekobox=228ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=201ms, nekobox=234ms, status=yes)
3. `AKUN-003-WPENG-VLESS-WS-80MS` (url=207ms, nekobox=256ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS` (url=216ms, nekobox=243ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=230ms, nekobox=257ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS` (url=225ms, nekobox=237ms, status=yes)
7. `AKUN-007-GO-DADDY-COM-LLC-VLESS-WS-90MS` (url=219ms, nekobox=263ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-86MS` (url=227ms, nekobox=250ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-67MS` (url=204ms, nekobox=234ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-103MS` (url=209ms, nekobox=244ms, status=yes)
11. `AKUN-011-466688-VLESS-WS-79MS` (url=231ms, status=HTTP 204)
12. `AKUN-012-466688-VLESS-WS-102MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-3666888-VLESS-WS-107MS` (url=320ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-112MS` (url=228ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-98MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-108MS` (url=212ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-142MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-GO-DADDY-COM-LLC-VLESS-WS-116MS` (url=222ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-87MS` (url=228ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-99MS` (url=226ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-108MS` (url=233ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-78MS` (url=201ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-245MS` (url=522ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-266MS` (url=547ms, status=HTTP 204)
25. `AKUN-026-ZVC-VLESS-WS-64MS` (url=293ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
