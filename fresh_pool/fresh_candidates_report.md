# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=212ms, nekobox=234ms, status=yes)
2. `AKUN-002-UK-GB-DCL-01-20191003-VLESS-WS-62MS` (url=221ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=214ms, nekobox=239ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-70MS` (url=200ms, nekobox=253ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=205ms, nekobox=181ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-106MS`
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-76MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS`
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-154MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-355MS` (url=665ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-358MS` (url=773ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-388MS` (url=824ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-402MS` (url=876ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-389MS` (url=851ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-404MS` (url=815ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-403MS` (url=853ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-369MS` (url=776ms, status=HTTP 204)
20. `AKUN-021-QZZ-VLESS-WS-563MS` (url=985ms, status=HTTP 204)
21. `AKUN-024-QZZ-VLESS-WS-531MS` (url=1228ms, status=HTTP 204)
22. `AKUN-027-UNKNOWN-VLESS-WS-734MS` (url=1217ms, status=HTTP 204)
23. `AKUN-032-QZZ-VLESS-WS-579MS` (url=1244ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-892MS` (url=1281ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
