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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=247ms, nekobox=247ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-79MS` (url=237ms, nekobox=251ms, status=yes)
3. `AKUN-003-877774-VLESS-WS-88MS` (url=247ms, nekobox=265ms, status=yes)
4. `AKUN-004-LEVIKOGJGFDD-VLESS-WS-73MS` (url=223ms, nekobox=262ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=237ms, nekobox=251ms, status=yes)
6. `AKUN-006-PAGES-VLESS-WS-118MS` (url=253ms, nekobox=278ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-111MS` (url=253ms, nekobox=266ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-160MS` (url=355ms, nekobox=320ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-101MS` (url=261ms, nekobox=270ms, status=yes)
10. `AKUN-010-LEVIKOGJGFDD-VLESS-WS-258MS` (url=590ms, nekobox=578ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-325MS` (url=1617ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-470MS` (url=856ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-453MS` (url=744ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-461MS` (url=892ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-483MS` (url=966ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-504MS` (url=830ms, status=HTTP 204)
17. `AKUN-020-UNKNOWN-VLESS-WS-479MS` (url=840ms, status=HTTP 204)
18. `AKUN-021-UNKNOWN-VLESS-WS-514MS` (url=884ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-476MS` (url=1221ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-481MS` (url=1172ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-475MS` (url=967ms, status=HTTP 204)
22. `AKUN-032-UNKNOWN-VLESS-WS-634MS` (url=5156ms, status=HTTP 204)
23. `AKUN-033-UNKNOWN-VLESS-WS-625MS` (url=1863ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-483MS` (url=800ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-651MS` (url=1743ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
