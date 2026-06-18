# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-65MS` (url=215ms, nekobox=243ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS` (url=221ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=200ms, nekobox=227ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-75MS` (url=214ms, nekobox=241ms, status=yes)
5. `AKUN-005-090227-VLESS-WS-92MS` (url=216ms, nekobox=247ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-121MS` (url=220ms, nekobox=250ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-118MS` (url=221ms, nekobox=237ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-77MS` (url=199ms, nekobox=237ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-130MS` (url=203ms, nekobox=181ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-98MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-150MS` (url=205ms, nekobox=186ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-378MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-359MS` (url=740ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-402MS` (url=2354ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-391MS` (url=813ms, status=HTTP 204)
16. `AKUN-016-INTEZIONET-VLESS-WS-388MS` (url=787ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-376MS` (url=828ms, status=HTTP 204)
18. `AKUN-018-INTEZIONET-VLESS-WS-418MS` (url=865ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-69MS` (url=848ms, status=HTTP 204)
20. `AKUN-021-INTEZIONET-VLESS-WS-448MS` (url=899ms, status=HTTP 204)
21. `AKUN-023-ARAD-VLESS-WS-590MS` (url=953ms, status=HTTP 204)
22. `AKUN-028-SELECTEL-NET-VLESS-WS-653MS` (url=1169ms, status=HTTP 204)
23. `AKUN-033-ONTHEWIFI-VLESS-WS-775MS` (url=1385ms, status=HTTP 204)
24. `AKUN-034-INTEZIONET-VLESS-WS-445MS` (url=811ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
