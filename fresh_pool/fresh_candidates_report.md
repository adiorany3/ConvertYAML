# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
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
1. `AKUN-001-CNAE-VLESS-WS-119MS` (url=267ms, nekobox=270ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-133MS` (url=249ms, nekobox=330ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-135MS` (url=270ms, nekobox=304ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-112MS` (url=249ms, nekobox=305ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-118MS` (url=290ms, nekobox=275ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-136MS` (url=269ms, nekobox=316ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-131MS` (url=294ms, nekobox=317ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-145MS` (url=274ms, nekobox=272ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-166MS` (url=245ms, nekobox=280ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-143MS` (url=261ms, nekobox=319ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-147MS` (url=241ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-324MS` (url=771ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-357MS` (url=728ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-360MS` (url=678ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-134MS` (url=314ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-377MS` (url=692ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-395MS` (url=769ms, status=HTTP 204)
18. `AKUN-023-CLOUDFLARE-VLESS-WS-337MS` (url=709ms, status=HTTP 204)
19. `AKUN-028-CLOUDFLARE-VLESS-WS-601MS` (url=938ms, status=HTTP 204)
20. `AKUN-029-CONFLU-VLESS-WS-354MS` (url=605ms, status=HTTP 204)
21. `AKUN-030-UNKNOWN-VLESS-WS-641MS` (url=908ms, status=HTTP 204)
22. `AKUN-032-DEV-VLESS-WS-453MS` (url=799ms, status=HTTP 204)
23. `AKUN-033-UNKNOWN-VLESS-WS-783MS` (url=1106ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
