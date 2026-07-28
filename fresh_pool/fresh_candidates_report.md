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
- Proxy di openclash_fresh_pool.yaml: 21

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
1. `AKUN-001-UNKNOWN-VLESS-WS-293MS` (url=561ms, nekobox=914ms, status=yes)
2. `AKUN-002-ICOOK-VLESS-WS-300MS` (url=795ms, nekobox=1074ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-306MS` (url=1493ms, nekobox=886ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-299MS` (url=822ms, nekobox=496ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-305MS` (url=608ms, nekobox=489ms, status=yes)
6. `AKUN-006-SKK-VLESS-WS-317MS` (url=586ms, nekobox=544ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-308MS` (url=467ms, nekobox=484ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-356MS` (url=656ms, nekobox=527ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-313MS` (url=567ms, nekobox=933ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-295MS` (url=470ms, nekobox=594ms, status=yes)
11. `AKUN-013-CLOUDFLARE-VLESS-WS-288MS` (url=1675ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-334MS` (url=586ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-585MS` (url=3955ms, status=HTTP 204)
14. `AKUN-017-CLOUDFLARE-VLESS-WS-303MS` (url=825ms, status=HTTP 204)
15. `AKUN-018-CLOUDFLARE-VLESS-WS-306MS` (url=851ms, status=HTTP 204)
16. `AKUN-019-UNKNOWN-VLESS-WS-411MS` (url=671ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-898MS` (url=1525ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
