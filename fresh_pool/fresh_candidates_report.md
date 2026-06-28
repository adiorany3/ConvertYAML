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
1. `AKUN-001-COMPREND-NET-VLESS-WS-67MS` (url=259ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-81MS` (url=228ms, nekobox=240ms, status=yes)
3. `AKUN-003-ORACLE-VLESS-WS-76MS` (url=214ms, nekobox=264ms, status=yes)
4. `AKUN-004-COMPREND-NET-VLESS-WS-62MS` (url=225ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=225ms, nekobox=256ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-72MS` (url=336ms, nekobox=266ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS` (url=209ms, nekobox=229ms, status=yes)
8. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-79MS` (url=216ms, nekobox=255ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-89MS` (url=218ms, nekobox=247ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-77MS` (url=217ms, nekobox=240ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-80MS` (url=233ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-93MS` (url=219ms, status=HTTP 204)
13. `AKUN-013-US-VLESS-WS-85MS` (url=227ms, status=HTTP 204)
14. `AKUN-014-MYBB-VLESS-WS-82MS` (url=326ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-73MS` (url=233ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-66MS` (url=204ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-81MS` (url=250ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-72MS` (url=227ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-73MS` (url=208ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-356MS` (url=747ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-361MS` (url=648ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-388MS` (url=858ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-400MS` (url=892ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-413MS` (url=832ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-416MS` (url=857ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
