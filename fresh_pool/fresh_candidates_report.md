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
1. `AKUN-001-ORACLE-VLESS-WS-131MS` (url=266ms, nekobox=284ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-128MS` (url=259ms, nekobox=289ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-135MS` (url=266ms, nekobox=292ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-132MS` (url=259ms, nekobox=303ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-138MS` (url=275ms, nekobox=285ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-153MS` (url=309ms, nekobox=312ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-139MS` (url=276ms, nekobox=298ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-131MS` (url=278ms, nekobox=298ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-141MS` (url=266ms, nekobox=324ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-160MS` (url=277ms, nekobox=295ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-155MS` (url=285ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-168MS` (url=269ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-143MS` (url=276ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-276MS` (url=531ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-281MS` (url=503ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-353MS` (url=686ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-373MS` (url=811ms, status=HTTP 204)
18. `AKUN-020-WPENG-VLESS-WS-396MS` (url=750ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-375MS` (url=773ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-385MS` (url=761ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-431MS` (url=4540ms, status=HTTP 204)
22. `AKUN-029-CLOUDFLARE-VLESS-WS-360MS` (url=762ms, status=HTTP 204)
23. `AKUN-030-UNKNOWN-VLESS-WS-354MS` (url=677ms, status=HTTP 204)
24. `AKUN-031-UNKNOWN-VLESS-WS-642MS` (url=1061ms, status=HTTP 204)
25. `AKUN-034-UNKNOWN-VLESS-WS-691MS` (url=1229ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
