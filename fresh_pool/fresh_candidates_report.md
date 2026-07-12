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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=222ms, nekobox=278ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=231ms, nekobox=308ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-81MS` (url=234ms, nekobox=288ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=263ms, nekobox=268ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS` (url=249ms, nekobox=288ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-81MS` (url=233ms, nekobox=270ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=250ms, nekobox=257ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS` (url=238ms, nekobox=274ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-82MS`
11. `AKUN-012-UNKNOWN-VLESS-WS-91MS` (url=358ms, status=HTTP 204)
12. `AKUN-013-UNKNOWN-VLESS-WS-93MS` (url=252ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-74MS` (url=231ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-105MS` (url=225ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-75MS` (url=278ms, status=HTTP 204)
16. `AKUN-017-ZOOM-VLESS-WS-86MS` (url=267ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-127MS` (url=199ms, status=HTTP 204)
18. `AKUN-019-466688-VLESS-WS-84MS` (url=236ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-136MS` (url=253ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-283MS` (url=5243ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-294MS` (url=681ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-301MS` (url=3774ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-265MS` (url=1596ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-310MS` (url=661ms, status=HTTP 204)
25. `AKUN-029-QZZ-VLESS-WS-253MS` (url=825ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
