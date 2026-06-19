# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 20
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-104-253-175-0-1-VLESS-WS-86MS`
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-105MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-85MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-109MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-71MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-360MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-350MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-385MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-402MS` (url=861ms, status=HTTP 204)
12. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-388MS` (url=839ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-397MS` (url=2434ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-423MS` (url=880ms, status=HTTP 204)
15. `AKUN-019-JISON-VLESS-WS-525MS` (url=946ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-359MS` (url=739ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-643MS` (url=919ms, status=HTTP 204)
18. `AKUN-023-CLOUDFLARE-VLESS-WS-630MS` (url=898ms, status=HTTP 204)
19. `AKUN-024-CLOUDFLARE-VLESS-WS-622MS` (url=876ms, status=HTTP 204)
20. `AKUN-031-UNKNOWN-VLESS-WS-757MS` (url=1092ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
