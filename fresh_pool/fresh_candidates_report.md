# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-UNKNOWN-VLESS-WS-80MS` (url=227ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=200ms, nekobox=211ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-120MS`
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS`
5. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-120MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-136MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-137MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-142MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-89MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-279MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-249MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-307MS` (url=574ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-298MS` (url=4382ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-297MS` (url=575ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-321MS` (url=706ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-380MS` (url=681ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-461MS` (url=805ms, status=HTTP 204)
18. `AKUN-027-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-91MS` (url=226ms, status=HTTP 204)
19. `AKUN-029-BIGCOMMERCE-VLESS-WS-463MS` (url=799ms, status=HTTP 204)
20. `AKUN-030-CLOUDFLARE-VLESS-WS-451MS` (url=754ms, status=HTTP 204)
21. `AKUN-034-CLOUDFLARE-VLESS-WS-492MS` (url=815ms, status=HTTP 204)
22. `AKUN-035-CLOUDFLARE-VLESS-WS-269MS` (url=563ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
