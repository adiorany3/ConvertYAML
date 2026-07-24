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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-85MS` (url=331ms, nekobox=387ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=274ms, nekobox=307ms, status=yes)
3. `AKUN-003-SPEEDTEST-VLESS-WS-84MS` (url=322ms, nekobox=191ms, status=no)
4. `AKUN-003-UNKNOWN-VLESS-WS-84MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-103MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-117MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-138MS`
9. `AKUN-008-LEVIKOGJGFDD-VLESS-WS-131MS`
10. `AKUN-011-SPEEDTEST-VLESS-WS-127MS` (url=284ms, nekobox=182ms, status=no)
11. `AKUN-009-UNKNOWN-VLESS-WS-92MS`
12. `AKUN-010-UNKNOWN-VLESS-WS-135MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-184MS` (url=435ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-184MS` (url=418ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-157MS` (url=469ms, status=HTTP 204)
16. `AKUN-017-ZVC-VLESS-WS-96MS` (url=365ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-173MS` (url=469ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-87MS` (url=337ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-318MS` (url=670ms, status=HTTP 204)
20. `AKUN-022-LEVIKOGJGFDD-VLESS-WS-315MS` (url=1981ms, status=HTTP 204)
21. `AKUN-023-SPEEDTEST-VLESS-WS-89MS` (url=661ms, status=HTTP 204)
22. `AKUN-024-SPEEDTEST-VLESS-WS-88MS` (url=407ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-458MS` (url=818ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-82MS` (url=633ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-601MS` (url=867ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
