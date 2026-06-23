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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS`
2. `AKUN-002-CLOUDFLARE-VLESS-WS-80MS`
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-85MS`
5. `AKUN-005-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-85MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-89MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS`
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-116MS`
10. `AKUN-011-CLOUDFLARE-VLESS-WS-119MS` (url=226ms, nekobox=177ms, status=no)
11. `AKUN-012-CLOUDFLARE-VLESS-WS-131MS` (url=221ms, nekobox=205ms, status=no)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-160MS` (url=219ms, nekobox=7175ms, status=no)
13. `AKUN-010-CLOUDFLARE-VLESS-WS-231MS`
14. `AKUN-015-CLOUDFLARE-VLESS-WS-228MS` (url=500ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-241MS` (url=554ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-246MS` (url=572ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-242MS` (url=492ms, status=HTTP 204)
18. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-255MS` (url=531ms, status=HTTP 204)
19. `AKUN-021-MICROSOFT-VLESS-WS-264MS` (url=539ms, status=HTTP 204)
20. `AKUN-025-APPLESERAJ-VLESS-WS-449MS` (url=694ms, status=HTTP 204)
21. `AKUN-028-UNKNOWN-VLESS-WS-462MS` (url=656ms, status=HTTP 204)
22. `AKUN-031-UNKNOWN-VLESS-WS-484MS` (url=1646ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
