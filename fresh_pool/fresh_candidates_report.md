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
1. `AKUN-001-OVH-VLESS-WS-82MS` (url=202ms, nekobox=224ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=231ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-88MS` (url=204ms, nekobox=227ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS` (url=232ms, nekobox=189ms, status=no)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-90MS` (url=204ms, nekobox=190ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-85MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-107MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-125MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-91MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-116MS`
11. `AKUN-009-UNKNOWN-VLESS-WS-108MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS`
13. `AKUN-013-PAGES-VLESS-WS-154MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-88MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-RMGYVPN-VLESS-WS-300MS` (url=597ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-353MS` (url=749ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-349MS` (url=773ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-650MS` (url=1011ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-676MS` (url=1107ms, status=HTTP 204)
20. `AKUN-030-CLOUDFLARE-VLESS-WS-799MS` (url=2908ms, status=HTTP 204)
21. `AKUN-033-TW-CLOUD-VLESS-WS-431MS` (url=3004ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
