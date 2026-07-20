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
1. `AKUN-001-UNKNOWN-VLESS-WS-81MS` (url=217ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-84MS` (url=228ms, nekobox=261ms, status=yes)
3. `AKUN-003-DIXONS-VLESS-WS-84MS` (url=227ms, nekobox=268ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=235ms, nekobox=280ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-85MS` (url=207ms, nekobox=241ms, status=yes)
6. `AKUN-006-466688-VLESS-WS-81MS` (url=235ms, nekobox=267ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-84MS` (url=222ms, nekobox=232ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS` (url=214ms, nekobox=239ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-74MS` (url=305ms, nekobox=274ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-87MS` (url=230ms, nekobox=244ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-97MS` (url=202ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-91MS` (url=252ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-103MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-112MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-113MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-83MS` (url=249ms, status=HTTP 204)
17. `AKUN-017-UK-GB-DCL-01-20191003-VLESS-WS-97MS` (url=241ms, status=HTTP 204)
18. `AKUN-018-WPENG-VLESS-WS-123MS` (url=208ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-115MS` (url=207ms, status=HTTP 204)
20. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-118MS` (url=232ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-134MS` (url=211ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-125MS` (url=253ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-118MS` (url=237ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-168MS` (url=222ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-187MS` (url=248ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
