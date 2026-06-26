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
1. `AKUN-001-ORACLE-VLESS-WS-119MS` (url=246ms, nekobox=307ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-106MS` (url=270ms, nekobox=329ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS` (url=296ms, nekobox=291ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-116MS` (url=240ms, nekobox=238ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-136MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-135MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-138MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-132MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-136MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-120MS` (url=286ms, nekobox=230ms, status=no)
11. `AKUN-009-DIGITALOCEAN-VLESS-WS-134MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-127MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-139MS` (url=304ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-125MS` (url=304ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-142MS` (url=333ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-157MS` (url=282ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-334MS` (url=692ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-339MS` (url=696ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-343MS` (url=693ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-325MS` (url=685ms, status=HTTP 204)
21. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-373MS` (url=753ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-284MS` (url=494ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-421MS` (url=750ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-437MS` (url=725ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-127MS` (url=328ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
