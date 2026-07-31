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
1. `AKUN-001-SPEEDTEST-VLESS-WS-125MS` (url=229ms, nekobox=222ms, status=no)
2. `AKUN-001-UNKNOWN-VLESS-WS-137MS`
3. `AKUN-002-UNKNOWN-VLESS-WS-130MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-138MS`
5. `AKUN-004-DEV-VLESS-WS-129MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-135MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-127MS`
8. `AKUN-007-DEV-VLESS-WS-129MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-127MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-137MS`
11. `AKUN-010-PAGES-VLESS-WS-191MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-197MS` (url=316ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-204MS` (url=327ms, status=HTTP 204)
14. `AKUN-014-NET-141-11-202-0-23-VLESS-WS-347MS` (url=699ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-251MS` (url=485ms, status=HTTP 204)
16. `AKUN-017-OPENAI-VLESS-WS-484MS` (url=1142ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-582MS` (url=1039ms, status=HTTP 204)
18. `AKUN-026-UNKNOWN-VLESS-WS-636MS` (url=1110ms, status=HTTP 204)
19. `AKUN-027-GAMEFICTOINSPEED-VLESS-WS-669MS` (url=1066ms, status=HTTP 204)
20. `AKUN-028-CLOUDFLARE-VLESS-WS-681MS` (url=1188ms, status=HTTP 204)
21. `AKUN-030-CLOUDFLARE-VLESS-WS-633MS` (url=1019ms, status=HTTP 204)
22. `AKUN-032-CLOUDFLARE-VLESS-WS-765MS` (url=1086ms, status=HTTP 204)
23. `AKUN-033-CLOUDFLARE-VLESS-WS-792MS` (url=1433ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-796MS` (url=1201ms, status=HTTP 204)
25. `AKUN-035-CLOUDFLARE-VLESS-WS-419MS` (url=866ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
