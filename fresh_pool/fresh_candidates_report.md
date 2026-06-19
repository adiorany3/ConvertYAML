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
1. `AKUN-001-090227-VLESS-WS-83MS` (url=230ms, nekobox=403ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-86MS` (url=229ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-95MS`
4. `AKUN-005-CLOUDFLARE-VLESS-WS-128MS` (url=235ms, nekobox=191ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-125MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-210MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-248MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-247MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-196MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-103MS`
12. `AKUN-015-CLOUDFLARE-VLESS-WS-131MS` (url=202ms, status=HTTP 204)
13. `AKUN-016-CLOUDFLARE-VLESS-WS-270MS` (url=555ms, status=HTTP 204)
14. `AKUN-017-CLOUDFLARE-VLESS-WS-249MS` (url=527ms, status=HTTP 204)
15. `AKUN-018-ZENFO-1-VLESS-WS-304MS` (url=2276ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-289MS` (url=594ms, status=HTTP 204)
17. `AKUN-024-CLOUDFLARE-VLESS-WS-419MS` (url=569ms, status=HTTP 204)
18. `AKUN-025-CLOUDFLARE-VLESS-WS-415MS` (url=580ms, status=HTTP 204)
19. `AKUN-026-CLOUDFLARE-VLESS-WS-419MS` (url=595ms, status=HTTP 204)
20. `AKUN-029-CLOUDFLARE-VLESS-WS-154MS` (url=236ms, status=HTTP 204)
21. `AKUN-032-CLOUDFLARE-VLESS-WS-371MS` (url=664ms, status=HTTP 204)
22. `AKUN-034-UNKNOWN-VLESS-WS-269MS` (url=586ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
