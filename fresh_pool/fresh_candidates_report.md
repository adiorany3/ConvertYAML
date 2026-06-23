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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-134MS` (url=269ms, nekobox=290ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-133MS` (url=270ms, nekobox=294ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-137MS` (url=255ms, nekobox=231ms, status=no)
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-138MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-136MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-145MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-146MS` (url=257ms, nekobox=248ms, status=no)
8. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-138MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-165MS` (url=238ms, nekobox=231ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-161MS` (url=242ms, nekobox=243ms, status=no)
11. `AKUN-011-DEV-VLESS-WS-143MS` (url=246ms, nekobox=248ms, status=no)
12. `AKUN-012-DEV-VLESS-WS-156MS` (url=245ms, nekobox=230ms, status=no)
13. `AKUN-007-UNKNOWN-VLESS-WS-156MS`
14. `AKUN-008-CLOUDFLARE-VLESS-WS-150MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-151MS` (url=248ms, nekobox=218ms, status=no)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-148MS` (url=245ms, nekobox=234ms, status=no)
17. `AKUN-009-CLOUDFLARE-VLESS-WS-347MS`
18. `AKUN-010-CLOUDFLARE-VLESS-WS-357MS`
19. `AKUN-019-CLOUDFLARE-VLESS-WS-358MS` (url=684ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-379MS` (url=773ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-392MS` (url=779ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-396MS` (url=802ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-394MS` (url=783ms, status=HTTP 204)
24. `AKUN-028-RS-RAPIDSEEDBOX-20190717-VLESS-WS-652MS` (url=1924ms, status=HTTP 204)
25. `AKUN-029-APPLESERAJ-VLESS-WS-642MS` (url=953ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
