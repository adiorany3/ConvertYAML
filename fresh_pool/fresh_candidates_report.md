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
1. `AKUN-001-UNKNOWN-VLESS-WS-143MS` (url=316ms, nekobox=316ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-145MS` (url=286ms, nekobox=314ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-136MS` (url=282ms, nekobox=312ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-149MS` (url=333ms, nekobox=352ms, status=yes)
5. `AKUN-005-PUBLICDOMAINREGISTRY-NET-VLESS-WS-150MS` (url=356ms, nekobox=2393ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-157MS` (url=383ms, nekobox=320ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-140MS` (url=354ms, nekobox=321ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-149MS` (url=343ms, nekobox=362ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-146MS` (url=275ms, nekobox=345ms, status=yes)
10. `AKUN-010-WPENG-VLESS-WS-148MS` (url=382ms, nekobox=307ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-156MS` (url=301ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-157MS` (url=294ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-153MS` (url=305ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-151MS` (url=356ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-146MS` (url=286ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-165MS` (url=365ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-163MS` (url=335ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-142MS` (url=285ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-168MS` (url=333ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-172MS` (url=339ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-364MS` (url=558ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-387MS` (url=735ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-361MS` (url=687ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-406MS` (url=866ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-405MS` (url=837ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
