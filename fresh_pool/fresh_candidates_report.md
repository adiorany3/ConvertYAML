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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-127MS` (url=259ms, nekobox=293ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-136MS` (url=270ms, nekobox=304ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-137MS` (url=265ms, nekobox=306ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-135MS` (url=286ms, nekobox=342ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-148MS` (url=284ms, nekobox=320ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-153MS` (url=275ms, nekobox=298ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-142MS` (url=270ms, nekobox=7172ms, status=no)
8. `AKUN-007-WEYRO-NET-VLESS-WS-153MS`
9. `AKUN-008-OVH-VLESS-WS-131MS`
10. `AKUN-009-WPENG-VLESS-WS-156MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-150MS`
12. `AKUN-012-466688-VLESS-WS-150MS` (url=266ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-157MS` (url=280ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-347MS` (url=686ms, status=HTTP 204)
15. `AKUN-017-CONFLU-VLESS-WS-347MS` (url=661ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-357MS` (url=706ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-367MS` (url=817ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-378MS` (url=755ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-365MS` (url=767ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-578MS` (url=958ms, status=HTTP 204)
21. `AKUN-025-UNKNOWN-VLESS-WS-629MS` (url=1000ms, status=HTTP 204)
22. `AKUN-028-CLOUDFLARE-VLESS-WS-724MS` (url=1231ms, status=HTTP 204)
23. `AKUN-029-CLOUDFLARE-VLESS-WS-731MS` (url=1290ms, status=HTTP 204)
24. `AKUN-031-CLOUDFLARE-VLESS-WS-674MS` (url=3461ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
