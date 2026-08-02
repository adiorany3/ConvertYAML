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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=228ms, nekobox=244ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=231ms, nekobox=182ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS`
4. `AKUN-003-008500-VLESS-WS-79MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS`
6. `AKUN-005-DEV-VLESS-WS-80MS`
7. `AKUN-007-UNKNOWN-VLESS-WS-106MS` (url=275ms, nekobox=7178ms, status=no)
8. `AKUN-006-DIGITALOCEAN-VLESS-WS-95MS`
9. `AKUN-009-DEV-VLESS-WS-114MS` (url=228ms, nekobox=189ms, status=no)
10. `AKUN-007-CLOUDFLARE-VLESS-WS-91MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-80MS` (url=227ms, nekobox=7174ms, status=no)
12. `AKUN-008-UNKNOWN-VLESS-WS-83MS`
13. `AKUN-009-CLOUDFLARE-VLESS-WS-109MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-116MS` (url=226ms, nekobox=181ms, status=no)
15. `AKUN-010-UNKNOWN-VLESS-WS-140MS`
16. `AKUN-016-UNKNOWN-VLESS-WS-102MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-120MS` (url=219ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-125MS` (url=360ms, status=HTTP 204)
19. `AKUN-019-RMGYVPN-VLESS-WS-277MS` (url=536ms, status=HTTP 204)
20. `AKUN-020-NODE2-VLESS-WS-114MS` (url=220ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-360MS` (url=3032ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-82MS` (url=227ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-524MS` (url=1023ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-532MS` (url=1069ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-523MS` (url=953ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
