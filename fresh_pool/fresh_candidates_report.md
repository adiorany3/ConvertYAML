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
1. `AKUN-001-UBI-VLESS-WS-132MS` (url=267ms, nekobox=287ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-133MS` (url=273ms, nekobox=286ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-140MS` (url=249ms, nekobox=295ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-144MS` (url=289ms, nekobox=294ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-144MS` (url=251ms, nekobox=299ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-147MS` (url=284ms, nekobox=329ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-145MS` (url=271ms, nekobox=302ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-139MS` (url=301ms, nekobox=311ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-147MS` (url=278ms, nekobox=289ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-133MS` (url=240ms, nekobox=221ms, status=no)
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-138MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-148MS` (url=299ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-146MS` (url=250ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-141MS` (url=273ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-159MS` (url=259ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-154MS` (url=267ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-158MS` (url=264ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-142MS` (url=263ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-169MS` (url=278ms, status=HTTP 204)
20. `AKUN-025-UNKNOWN-VLESS-WS-369MS` (url=690ms, status=HTTP 204)
21. `AKUN-026-UNKNOWN-VLESS-WS-354MS` (url=713ms, status=HTTP 204)
22. `AKUN-027-UNKNOWN-VLESS-WS-369MS` (url=712ms, status=HTTP 204)
23. `AKUN-028-UNKNOWN-VLESS-WS-380MS` (url=766ms, status=HTTP 204)
24. `AKUN-029-UNKNOWN-VLESS-WS-381MS` (url=777ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-395MS` (url=777ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
