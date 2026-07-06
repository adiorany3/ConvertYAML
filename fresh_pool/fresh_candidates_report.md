# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 17
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
1. `AKUN-001-ZVC-VLESS-WS-83MS` (url=217ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-91MS` (url=199ms, nekobox=252ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=219ms, nekobox=189ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-90MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-95MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-116MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-106MS` (url=211ms, nekobox=199ms, status=no)
8. `AKUN-006-TANG-NET-VLESS-WS-94MS`
9. `AKUN-010-DEV-VLESS-WS-99MS` (url=204ms, nekobox=172ms, status=no)
10. `AKUN-007-UNKNOWN-VLESS-WS-259MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-268MS`
12. `AKUN-014-UNKNOWN-VLESS-WS-267MS` (url=577ms, nekobox=390ms, status=no)
13. `AKUN-009-CLOUDFLARE-VLESS-WS-268MS`
14. `AKUN-010-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-72MS`
15. `AKUN-017-CLOUDFLARE-VLESS-WS-234MS` (url=496ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-417MS` (url=708ms, status=HTTP 204)
17. `AKUN-023-CLOUDFLARE-VLESS-WS-222MS` (url=3047ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
