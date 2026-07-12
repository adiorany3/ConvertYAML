# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=244ms, nekobox=272ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=237ms, nekobox=253ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=216ms, nekobox=260ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS` (url=220ms, nekobox=272ms, status=yes)
5. `AKUN-005-VULTR-VLESS-WS-73MS` (url=230ms, nekobox=257ms, status=yes)
6. `AKUN-006-HETZNER-VLESS-WS-70MS` (url=268ms, nekobox=293ms, status=yes)
7. `AKUN-007-OVH-VLESS-WS-83MS` (url=290ms, nekobox=261ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-85MS` (url=237ms, nekobox=271ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-79MS` (url=219ms, nekobox=261ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-105MS` (url=234ms, nekobox=271ms, status=yes)
11. `AKUN-011-ZOOM-VLESS-WS-90MS` (url=285ms, status=HTTP 204)
12. `AKUN-012-466688-VLESS-WS-85MS` (url=236ms, status=HTTP 204)
13. `AKUN-014-US-VLESS-WS-106MS` (url=264ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-91MS` (url=227ms, status=HTTP 204)
15. `AKUN-016-466688-VLESS-WS-118MS` (url=239ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-89MS` (url=244ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-278MS` (url=632ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-294MS` (url=3177ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-270MS` (url=691ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-292MS` (url=671ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-294MS` (url=2016ms, status=HTTP 204)
22. `AKUN-026-QZZ-VLESS-WS-220MS` (url=704ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-461MS` (url=778ms, status=HTTP 204)
24. `AKUN-028-UNKNOWN-VLESS-WS-529MS` (url=877ms, status=HTTP 204)
25. `AKUN-029-GAMEFICTOINSPEED-VLESS-WS-516MS` (url=919ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
