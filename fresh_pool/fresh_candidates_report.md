# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 25

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
1. `AKUN-001-ICOOK-VLESS-WS-99MS`
2. `AKUN-002-CLOUDFLARE-VLESS-WS-107MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-110MS`
4. `AKUN-004-DEV-VLESS-WS-112MS`
5. `AKUN-005-ZVC-VLESS-WS-116MS`
6. `AKUN-006-DEV-VLESS-WS-118MS`
7. `AKUN-007-HOSTINGER-VLESS-WS-126MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-137MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-107MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-161MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-147MS` (url=234ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-145MS` (url=351ms, status=HTTP 204)
13. `AKUN-015-UNKNOWN-VLESS-WS-179MS` (url=356ms, status=HTTP 204)
14. `AKUN-016-UNKNOWN-VLESS-WS-140MS` (url=318ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-183MS` (url=311ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-200MS` (url=373ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-292MS` (url=2850ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-289MS` (url=676ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-105MS` (url=232ms, status=HTTP 204)
20. `AKUN-028-CLOUDFLARE-VLESS-WS-503MS` (url=922ms, status=HTTP 204)
21. `AKUN-034-CLOUDFLARE-VLESS-WS-576MS` (url=971ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
