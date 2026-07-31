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
1. `AKUN-001-SPEEDTEST-VLESS-WS-60MS` (url=253ms, nekobox=172ms, status=no)
2. `AKUN-001-UNKNOWN-VLESS-WS-66MS`
3. `AKUN-002-MEDIUM-VLESS-WS-70MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-63MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS`
6. `AKUN-005-ALIBABA-VLESS-WS-64MS`
7. `AKUN-006-LEVIKOGJGFDD-VLESS-WS-69MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS`
9. `AKUN-009-SPEEDTEST-VLESS-WS-62MS` (url=239ms, nekobox=175ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS`
11. `AKUN-009-UNKNOWN-VLESS-WS-67MS`
12. `AKUN-010-PAGES-VLESS-WS-67MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-83MS` (url=227ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-96MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-123MS` (url=259ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-143MS` (url=320ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-89MS` (url=780ms, status=HTTP 204)
18. `AKUN-018-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-151MS` (url=262ms, status=HTTP 204)
19. `AKUN-019-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-122MS` (url=1600ms, status=HTTP 204)
20. `AKUN-021-DIGITALOCEAN-VLESS-WS-85MS` (url=235ms, status=HTTP 204)
21. `AKUN-022-LEVIKOGJGFDD-VLESS-WS-72MS` (url=223ms, status=HTTP 204)
22. `AKUN-023-ADF-VLESS-WS-104MS` (url=247ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-109MS` (url=248ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-251MS` (url=525ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-197MS` (url=475ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
