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
1. `AKUN-001-HOSTWINDS-17-7-VLESS-WS-302MS` (url=503ms, nekobox=500ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-300MS` (url=513ms, nekobox=515ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-304MS` (url=505ms, nekobox=540ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-315MS`
5. `AKUN-005-LEVIKOGJGFDD-VLESS-WS-308MS`
6. `AKUN-006-UNKNOWN-VLESS-WS-317MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-323MS`
8. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-328MS`
9. `AKUN-009-FMN5-RENTED-NET2-VLESS-WS-315MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-329MS`
11. `AKUN-013-UNKNOWN-VLESS-WS-312MS` (url=493ms, status=HTTP 204)
12. `AKUN-014-UNKNOWN-VLESS-WS-330MS` (url=551ms, status=HTTP 204)
13. `AKUN-015-EU-VLESS-WS-333MS` (url=563ms, status=HTTP 204)
14. `AKUN-016-LEVIKOGJGFDD-VLESS-WS-373MS` (url=679ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-326MS` (url=511ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-315MS` (url=494ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-579MS` (url=1060ms, status=HTTP 204)
18. `AKUN-023-CLOUDFLARE-VLESS-WS-388MS` (url=586ms, status=HTTP 204)
19. `AKUN-024-CLOUDFLARE-VLESS-WS-502MS` (url=3811ms, status=HTTP 204)
20. `AKUN-025-CLOUDFLARE-VLESS-WS-815MS` (url=1000ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
