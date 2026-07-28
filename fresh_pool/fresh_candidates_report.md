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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=274ms, nekobox=266ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=221ms, nekobox=263ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-62MS` (url=287ms, nekobox=253ms, status=yes)
4. `AKUN-004-LEVIKOGJGFDD-VLESS-WS-72MS` (url=233ms, nekobox=261ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-71MS` (url=241ms, nekobox=274ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-58MS` (url=272ms, nekobox=262ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-71MS` (url=278ms, nekobox=278ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-98MS` (url=292ms, nekobox=260ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-101MS` (url=263ms, nekobox=349ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS` (url=333ms, nekobox=366ms, status=yes)
11. `AKUN-011-OPENAI-VLESS-WS-66MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-117MS` (url=336ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-80MS` (url=277ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-113MS` (url=313ms, status=HTTP 204)
15. `AKUN-015-LEVIKOGJGFDD-VLESS-WS-160MS` (url=303ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-127MS` (url=327ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-219MS` (url=435ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-223MS` (url=459ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-254MS` (url=537ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-263MS` (url=533ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-258MS` (url=4296ms, status=HTTP 204)
22. `AKUN-023-BNCGT-VLESS-WS-365MS` (url=648ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-407MS` (url=1170ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-452MS` (url=765ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-457MS` (url=840ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
