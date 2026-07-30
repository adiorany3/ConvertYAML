# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 19
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 23

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=201ms, nekobox=242ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-68MS` (url=218ms, nekobox=237ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=205ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=199ms, nekobox=231ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-64MS` (url=222ms, nekobox=175ms, status=no)
6. `AKUN-005-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-72MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-70MS`
8. `AKUN-007-ZOOM-VLESS-WS-118MS`
9. `AKUN-009-SPEEDTEST-VLESS-WS-164MS` (url=218ms, nekobox=183ms, status=no)
10. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-141MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-116MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-190MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-115MS` (url=208ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-105MS` (url=195ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-217MS` (url=472ms, status=HTTP 204)
16. `AKUN-020-TW-CLOUD-VLESS-WS-175MS` (url=770ms, status=HTTP 204)
17. `AKUN-029-CLOUDFLARE-VLESS-WS-405MS` (url=662ms, status=HTTP 204)
18. `AKUN-030-UNKNOWN-VLESS-WS-506MS` (url=839ms, status=HTTP 204)
19. `AKUN-035-CLOUDFLARE-VLESS-WS-297MS` (url=712ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
