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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-127MS` (url=296ms, nekobox=346ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-131MS` (url=281ms, nekobox=312ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-134MS` (url=282ms, nekobox=299ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-142MS` (url=285ms, nekobox=330ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-140MS` (url=291ms, nekobox=367ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-133MS` (url=266ms, nekobox=305ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-149MS` (url=307ms, nekobox=319ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-142MS` (url=297ms, nekobox=304ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-145MS` (url=273ms, nekobox=248ms, status=no)
10. `AKUN-009-UNKNOWN-VLESS-WS-155MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-154MS`
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-136MS` (url=301ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-147MS` (url=378ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-166MS` (url=280ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-160MS` (url=279ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-194MS` (url=341ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-169MS` (url=296ms, status=HTTP 204)
18. `AKUN-018-LEVIKOGJGFDD-VLESS-WS-171MS` (url=339ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-204MS` (url=346ms, status=HTTP 204)
20. `AKUN-020-PAGES-VLESS-WS-172MS` (url=280ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-191MS` (url=415ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-227MS` (url=420ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-358MS` (url=792ms, status=HTTP 204)
24. `AKUN-024-LEVIKOGJGFDD-VLESS-WS-358MS` (url=732ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-366MS` (url=802ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
