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
- Proxy di openclash_fresh_pool.yaml: 24

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
1. `AKUN-001-UNKNOWN-VLESS-WS-75MS` (url=206ms, nekobox=250ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-88MS` (url=217ms, nekobox=243ms, status=yes)
3. `AKUN-003-PAGES-VLESS-WS-93MS` (url=202ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-93MS` (url=229ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=219ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-107MS` (url=212ms, nekobox=242ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-126MS` (url=236ms, nekobox=250ms, status=yes)
8. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-105MS` (url=225ms, nekobox=256ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-108MS` (url=225ms, nekobox=251ms, status=yes)
10. `AKUN-010-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-130MS` (url=1544ms, nekobox=1412ms, status=yes)
11. `AKUN-012-CLOUDFLARE-VLESS-WS-95MS` (url=199ms, status=HTTP 204)
12. `AKUN-015-CLOUDFLARE-VLESS-WS-363MS` (url=755ms, status=HTTP 204)
13. `AKUN-018-CLOUDFLARE-VLESS-WS-628MS` (url=1073ms, status=HTTP 204)
14. `AKUN-019-UNKNOWN-VLESS-WS-616MS` (url=1048ms, status=HTTP 204)
15. `AKUN-021-CLOUDFLARE-VLESS-WS-697MS` (url=1191ms, status=HTTP 204)
16. `AKUN-023-CLOUDFLARE-VLESS-WS-781MS` (url=1220ms, status=HTTP 204)
17. `AKUN-027-AE-ORYXLABS-20081128-VLESS-WS-667MS` (url=1152ms, status=HTTP 204)
18. `AKUN-029-CLOUDFLARE-VLESS-WS-803MS` (url=1280ms, status=HTTP 204)
19. `AKUN-032-UNKNOWN-VLESS-WS-849MS` (url=1320ms, status=HTTP 204)
20. `AKUN-035-TW-CLOUD-VLESS-WS-433MS` (url=3744ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
