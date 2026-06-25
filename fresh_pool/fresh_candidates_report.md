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
1. `AKUN-001-UNKNOWN-VLESS-WS-130MS` (url=263ms, nekobox=292ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-136MS` (url=266ms, nekobox=279ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-128MS` (url=234ms, nekobox=225ms, status=no)
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-143MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-144MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-145MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-157MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-142MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-159MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-147MS` (url=245ms, nekobox=224ms, status=no)
11. `AKUN-011-UNKNOWN-VLESS-WS-150MS` (url=262ms, nekobox=7176ms, status=no)
12. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-133MS`
13. `AKUN-010-UNKNOWN-VLESS-WS-178MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-155MS` (url=285ms, status=HTTP 204)
15. `AKUN-015-RS-RAPIDSEEDBOX-20190717-VLESS-WS-132MS` (url=277ms, status=HTTP 204)
16. `AKUN-016-US-VLESS-WS-140MS` (url=264ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-145MS` (url=257ms, status=HTTP 204)
18. `AKUN-018-154-83-95-0-154-83-95-25-VLESS-WS-171MS` (url=262ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-145MS` (url=282ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-275MS` (url=362ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-354MS` (url=680ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-377MS` (url=736ms, status=HTTP 204)
23. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-370MS` (url=756ms, status=HTTP 204)
24. `AKUN-027-RS-RAPIDSEEDBOX-20190717-VLESS-WS-394MS` (url=749ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-342MS` (url=3374ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
