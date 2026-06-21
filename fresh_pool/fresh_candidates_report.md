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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-73MS` (url=238ms, nekobox=274ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-77MS` (url=240ms, nekobox=262ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=257ms, nekobox=265ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=268ms, nekobox=265ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS` (url=245ms, nekobox=272ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS` (url=230ms, nekobox=272ms, status=yes)
7. `AKUN-007-VULTR-VLESS-WS-81MS` (url=241ms, nekobox=271ms, status=yes)
8. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-74MS` (url=275ms, nekobox=268ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-121MS` (url=244ms, nekobox=257ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-78MS` (url=307ms, nekobox=278ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-260MS` (url=547ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-284MS` (url=656ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-302MS` (url=606ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-294MS` (url=619ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-267MS` (url=561ms, status=HTTP 204)
16. `AKUN-017-CONFLU-VLESS-WS-342MS` (url=562ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-320MS` (url=647ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-547MS` (url=891ms, status=HTTP 204)
19. `AKUN-034-CLOUDFLARE-VLESS-WS-653MS` (url=1082ms, status=HTTP 204)
20. `AKUN-035-CLOUDFLARE-VLESS-WS-757MS` (url=1267ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
